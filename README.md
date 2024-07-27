# Interactive Tumor Growth Simulator
## Overview
The Interactive Tumor Growth Simulator is a Python-based tool that models and visualizes the growth of tumors within a grid. Users can interact with the simulation by adjusting parameters such as the cell proliferation rate, nutrient availability, and simulation time steps. This tool provides real-time visualizations and metrics to understand the dynamics of tumor growth.

## Features
Interactive Sliders: Adjust proliferation rate, nutrient availability, and time steps.
Dynamic Visualizations: Includes 3D surface plots, heatmaps, and timeline graphs.
Summary Dashboard: Displays key metrics and warnings.
Educational Content: Provides context with additional information and images.

## Installation
To set up the Interactive Tumor Growth Simulator, follow these steps:
- Clone the Repository:
```
git clone https://github.com/yourusername/tumor-growth-simulator.git
cd tumor-growth-simulator
 ```
- Create a Virtual Environment:
```
python -m venv venv
```
- Activate the Virtual Environment:
  * Windows
```
venv\Scripts\activate
```
  * macOs/Linux
```
source venv/bin/activate
```
- Install Required Packages
```
pip install -r requirements.txt
```
## Usage
- Run the Simulation:

Launch the Jupyter notebook to interact with the simulator.
```
jupyter notebook
```
- Interact with the Simulator:

Open the notebook and use the sliders to adjust parameters:

Proliferation Rate: Controls how quickly the tumor cells proliferate.
Nutrient Availability: Affects the growth based on nutrient levels.
Time Step: Navigate through different simulation steps.
The visualizations and metrics will update in real-time based on your inputs.

## Testing
To test the simulator:

- Run the Notebook Cells:

Ensure all cells execute without errors in the Jupyter notebook.

- Verify Visualizations:

Check that the 3D surface plots, heatmaps, and timelines update correctly with parameter changes.

- Check Metrics:

Confirm that the summary dashboard displays accurate metrics and warnings.

- Contributing
Feel free to submit issues or pull requests to contribute to the project. Ensure you follow the guidelines and test any changes thoroughly.

- License
This project is licensed under the MIT License. See the  [MIT LICENSE](https://github.com/Sushil2k4/Tumor-Growth-Simulator/blob/main/LICENSE) FILE for details.

Acknowledgements
NumPy: For numerical operations.
Plotly: For interactive visualizations.
Matplotlib: For heatmaps and timeline graphs.
ipywidgets: For interactive controls.
