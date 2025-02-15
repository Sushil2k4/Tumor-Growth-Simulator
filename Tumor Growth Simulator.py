import numpy as np
import plotly.graph_objects as go
from ipywidgets import interact, FloatSlider, IntSlider, VBox, HBox, Output
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import display, HTML
import plotly.io as pio

# Grid and parameters
GRID_SIZE = (100, 100)
INITIAL_TUMOR_SIZE = 5
PROLIFERATION_RATE = 0.1
NUTRIENT_AVAILABILITY = 0.1
NUTRIENT_THRESHOLD = 0.05
MAX_TIME_STEPS = 100

# Initialize grid
grid = np.zeros(GRID_SIZE)
center = (GRID_SIZE[0] // 2, GRID_SIZE[1] // 2)
grid[center[0] - INITIAL_TUMOR_SIZE:center[0] + INITIAL_TUMOR_SIZE,
     center[1] - INITIAL_TUMOR_SIZE:center[1] + INITIAL_TUMOR_SIZE] = 1

# Output widgets
output, heatmap_output, timeline_output, summary_output, info_output = Output(), Output(), Output(), Output(), Output()

def update(frame_num, rate, nutrient):
    global grid
    
    new_grid = grid.copy()
    tumor_cells = np.argwhere(grid == 1)
    
    if nutrient > NUTRIENT_THRESHOLD:
        for i, j in tumor_cells:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Only cardinal directions
                ni, nj = i + dx, j + dy
                if 0 <= ni < GRID_SIZE[0] and 0 <= nj < GRID_SIZE[1] and grid[ni, nj] == 0:
                    if np.random.random() < rate:
                        new_grid[ni, nj] = 1
    
    grid[:] = new_grid
    tumor_count = np.sum(grid)
    growth_rate = tumor_count / (frame_num + 1)
    
    # 3D Surface plot
    fig = go.Figure(data=[go.Surface(z=grid, colorscale='Viridis')])
    fig.update_layout(title=f'Time Step: {frame_num}',
                      scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Tumor Cells'))
    pio.show(fig, renderer="iframe")
    
    # Heatmap
    with heatmap_output:
        heatmap_output.clear_output()
        plt.imshow(grid, cmap='hot', interpolation='nearest')
        plt.title(f'Heatmap at Time Step: {frame_num}')
        plt.colorbar()
        plt.show()
    
    # Tumor Growth Timeline
    with timeline_output:
        timeline_output.clear_output()
        plt.plot(frame_num, tumor_count, 'bo')
        plt.title('Tumor Growth Over Time')
        plt.xlabel('Time Step')
        plt.ylabel('Total Tumor Cells')
        plt.show()
    
    # Summary Dashboard
    with summary_output:
        summary_output.clear_output()
        summary_html = f"""
        <div style='padding: 10px; border: 2px solid black; background-color: #f9f9f9;'>
            <h2 style='color: #2e6da4;'>Summary Dashboard</h2>
            <p><strong>Total Tumor Cells:</strong> <span style='color: #d9534f;'>{tumor_count}</span></p>
            <p><strong>Growth Rate:</strong> <span style='color: #5bc0de;'>{growth_rate:.2f} cells per time step</span></p>
            <p><strong>Current Time Step:</strong> {frame_num}</p>
            <p><strong>Proliferation Rate:</strong> {rate:.2f}</p>
            <p><strong>Nutrient Availability:</strong> {nutrient:.2f}</p>
        </div>
        """
        display(HTML(summary_html))
    
    return fig

# Interactive controls
rate_slider = FloatSlider(min=0, max=1, step=0.01, value=PROLIFERATION_RATE, description='Proliferation Rate')
nutrient_slider = FloatSlider(min=0, max=1, step=0.01, value=NUTRIENT_AVAILABILITY, description='Nutrient Availability')
time_slider = IntSlider(min=0, max=MAX_TIME_STEPS, step=1, value=0, description='Time Step')

controls = VBox([time_slider, rate_slider, nutrient_slider])
display(VBox([controls, HBox([output, heatmap_output]), HBox([timeline_output]), summary_output, info_output]))
interact(update, frame_num=time_slider, rate=rate_slider, nutrient=nutrient_slider)
