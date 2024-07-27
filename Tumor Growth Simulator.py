#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import plotly.graph_objects as go
from ipywidgets import interact, FloatSlider, IntSlider, HBox, VBox, Output
import plotly.io as pio
from IPython.display import display, HTML
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the grid size and initial parameters
grid_size = (100, 100)
initial_tumor_size = 5
cell_proliferation_rate = 0.1
nutrient_availability = 0.1
nutrient_availability_threshold = 0.05
max_time_steps = 100

# Initialize the grid
grid = np.zeros(grid_size)

# Place the initial tumor
center = (grid_size[0] // 2, grid_size[1] // 2)
grid[center[0] - initial_tumor_size:center[0] + initial_tumor_size,
     center[1] - initial_tumor_size:center[1] + initial_tumor_size] = 1

# Output widgets for warnings and information
output = Output()
heatmap_output = Output()
timeline_output = Output()
summary_output = Output()
additional_info_output = Output()

# Define the update function
def update(frame_num, rate, nutrient):
    global grid  # Ensure we modify the global grid variable
    
    # Copy the grid to avoid modifying it while iterating
    new_grid = np.copy(grid)
    total_tumor_cells = np.sum(grid)
    
    # Iterate over each cell in the grid
    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            # Check if the current cell is a tumor cell
            if grid[i, j] == 1:
                # Check nutrient availability
                if nutrient > nutrient_availability_threshold:
                    # Proliferate into adjacent empty cells
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue  # Skip the current cell
                            # Calculate neighbor coordinates
                            ni, nj = i + dx, j + dy
                            # Check if neighbor is within grid bounds and empty
                            if 0 <= ni < grid_size[0] and 0 <= nj < grid_size[1] and grid[ni, nj] == 0:
                                # Proliferate with a probability determined by the cell proliferation rate
                                if np.random.random() < rate:
                                    new_grid[ni, nj] = 1

    # Update the grid with the new state
    grid = new_grid
    
    # Create 3D surface plot
    x, y = np.meshgrid(np.arange(grid_size[0]), np.arange(grid_size[1]))
    fig = go.Figure(data=[go.Surface(z=grid, colorscale='Viridis')])
    fig.update_layout(title=f'Time step: {frame_num}',
                      scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Tumor Cells'))
    
    pio.show(fig, renderer="iframe")  # Display the figure
    
    # Calculate metrics
    total_tumor_cells = np.sum(grid)
    growth_rate = total_tumor_cells / (frame_num + 1)
    percentage_growth = (total_tumor_cells / (grid_size[0] * grid_size[1])) * 100
    
    # Display warnings and metrics
    with output:
        output.clear_output()
        if total_tumor_cells > 0.5 * grid_size[0] * grid_size[1]:
            display(HTML("<p style='color:red;'>Warning: The tumor has grown very large!</p>"))
    
    # Update heatmap
    with heatmap_output:
        heatmap_output.clear_output()
        plt.imshow(grid, cmap='hot', interpolation='nearest')
        plt.title(f'Heatmap at Time Step: {frame_num}')
        plt.colorbar()
        plt.show()
    
    # Update timeline
    with timeline_output:
        timeline_output.clear_output()
        plt.plot(frame_num, total_tumor_cells, 'bo')
        plt.title('Tumor Cells Over Time')
        plt.xlabel('Time Step')
        plt.ylabel('Total Tumor Cells')
        plt.show()
    
    # Update summary dashboard
    with summary_output:
        summary_output.clear_output()
        summary_html = f"""
        <div style='padding: 10px; border: 2px solid black; background-color: #f9f9f9;'>
            <h2 style='color: #2e6da4;'>Summary Dashboard</h2>
            <p><strong>Total Tumor Cells:</strong> <span style='color: #d9534f;'>{total_tumor_cells}</span></p>
            <p><strong>Growth Rate:</strong> <span style='color: #5bc0de;'>{growth_rate:.2f} cells per time step</span></p>
            <p><strong>Percentage Growth:</strong> <span style='color: #5cb85c;'>{percentage_growth:.2f}%</span></p>
            <p><strong>Current Time Step:</strong> {frame_num}</p>
            <p><strong>Proliferation Rate:</strong> {rate:.2f}</p>
            <p><strong>Nutrient Availability:</strong> {nutrient:.2f}</p>
        </div>
        """
        display(HTML(summary_html))
    
    # Additional information with sketches and doctor image
    with additional_info_output:
        additional_info_output.clear_output()
        additional_info_html = f"""
        <div style='display: flex; align-items: center; padding: 10px; border: 2px solid #ddd; background-color: #fff;'>
            <div style='flex: 1;'>
                <h3 style='color: #3c763d;'>Additional Information</h3>
                <p><img src='https://st.depositphotos.com/1806106/4006/i/450/depositphotos_40068077-stock-photo-cancer-cell.jpg' alt='Cell Diagram' style='width:200px;height:auto;float:right;margin-left:10px;'>Tumor growth is influenced by various factors including cell proliferation rate and nutrient availability. Understanding these dynamics can help in devising better treatment strategies.</p>
                <p>For more detailed insights, refer to the cell diagram on the right which explains the different phases of cell growth and division.</p>
            </div>
            <div style='flex: 0 0 auto;'>
                <img src='https://img.freepik.com/free-vector/hand-drawn-doctor-cartoon-illustration_23-2150682053.jpg' alt='Cartoon Doctor' style='width:150px;height:auto;'>
            </div>
        </div>
        """
        display(HTML(additional_info_html))
    
    return fig  # Return the figure object

# Create interactive sliders
rate_slider = FloatSlider(min=0, max=1, step=0.01, value=cell_proliferation_rate, description='Proliferation Rate')
nutrient_slider = FloatSlider(min=0, max=1, step=0.01, value=nutrient_availability, description='Nutrient Availability')
time_slider = IntSlider(min=0, max=max_time_steps, step=1, value=0, description='Time Step')

# Set up the interactive plot
controls = VBox([time_slider, rate_slider, nutrient_slider])
display(VBox([controls, HBox([output, heatmap_output]), HBox([timeline_output]), summary_output, additional_info_output]))
interact(update, frame_num=time_slider, rate=rate_slider, nutrient=nutrient_slider)


# In[ ]:
#thanks



