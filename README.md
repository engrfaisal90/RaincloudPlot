# RainCloudPlot

`RainCloudPlot` is a Python class designed to create **RainCloud plots**, which combine a half-violin plot, box plot, and strip plot to display the distribution of data. The class allows for customization of axis labels, titles, color palettes, and more.

## Table of Contents
- [Installation](#installation)
- [Dependencies](#dependencies)
- [Class Usage](#class-usage)
- [Method Descriptions](#method-descriptions)
- [Example](#example)
- [Customization](#customization)

---

## Installation

1. Clone the repository or download the Python script that contains the `RainCloudPlot` class.
2. Install the required dependencies via pip:

    ```bash
    pip install numpy pandas seaborn matplotlib ptitprince
    ```

---

## Dependencies

The class requires the following Python packages:
- `numpy` (for numerical operations)
- `pandas` (for DataFrame manipulation)
- `seaborn` (for advanced visualizations)
- `matplotlib` (for plotting)
- `ptitprince` (for half-violin plots)

---

## Class Usage

The `RainCloudPlot` class allows for the creation of comparative visualizations that combine strip plots, box plots, and half-violin plots. You can visualize the distribution of two or more groups using these visual elements.

### Class Initialization

```python
plotter = RainCloudPlot(data=df, jitter_strength=0.05, palette="Set2")
```

## Parameters:

### Initialization Parameters:
- `data`: A pandas DataFrame with two or more columns representing the groups for comparison.
- `jitter_strength`: Controls the amount of jitter applied to the strip plot points for better visualization.
- `palette`: A color palette for customizing the look of the plots.

### Method to Generate Plot:
```python
plotter.generate_plot(
    subplots_list, 
    show_x, 
    show_y, 
    show_xlabel, 
    show_ylabel, 
    titles, 
    x_labels, 
    y_labels, 
    palette, 
    show_border
)
```

## Parameters:

### For `generate_plot()` Method:
- **`subplots_list`**: A list defining which plots to include (options: `'strip'`, `'box'`, `'violin'`).
- **`show_x`, `show_y`**: Lists that define whether to display the x-axis or y-axis ticks.
- **`show_xlabel`, `show_ylabel`**: Lists that define whether to show x-axis and y-axis labels.
- **`titles`**: A list of titles for each subplot.
- **`x_labels`, `y_labels`**: A list of labels for the x-axis and y-axis for each subplot.
- **`palette`**: Custom color palette for the plots (optional).
- **`show_border`**: A list of dictionaries controlling the visibility of plot borders (spines).

---

## Method Descriptions:

- **`generate_plot()`**: This method generates a combination of RainCloud plots (half-violin plot, box plot, and strip plot) based on the specified configurations.

- **`_strip_plot()`**: Creates a strip plot with jittered points, connecting the groups with lines.

- **`_box_plot()`**: Draws a box plot to summarize the central tendency and distribution of data.

- **`_half_violin_plot()`**: Draws a half-violin plot showing the density distribution of the data.
  
---

## Example:

```python
import pandas as pd
import numpy as np

# Example Data
np.random.seed(42)
df = pd.DataFrame({
    "Group 1": np.random.normal(3, 0.5, 20),  # Random data for Group 1
    "Group 2": np.random.normal(4, 0.5, 20)   # Random data for Group 2
})

# Instantiate the RainCloudPlot class (assuming it is defined elsewhere)
plotter = RainCloudPlot(data=df, jitter_strength=0.05)

# Generate the RainCloud plot
plotter.generate_plot(
    ['strip', 'box', 'violin'],  # Types of plots to generate: strip, box, and violin plots
    show_x=[False, False, True],  # Show x-axis ticks only for the violin plot
    show_y=[True, False, False],  # Show y-axis ticks only for the strip plot
    show_xlabel=[False, False, True],  # Show x-axis label for the violin plot
    show_ylabel=[True, False, False],  # Show y-axis label for the strip plot
    titles=["Strip Plot", "Box Plot", "Violin Plot"],  # Titles for the subplots
    x_labels=["", "", "Group"],  # X-axis labels, only for the violin plot
    y_labels=["Value", "", ""],  # Y-axis labels, only for the strip plot
    palette=["#1f77b4", "#ff7f0e"],  # Custom color palette (blue for Group 1, orange for Group 2)
    show_border=[
        {'top': True, 'bottom': True, 'left': True, 'right': False},  # Border control for strip plot
        {'top': True, 'bottom': True, 'left': False, 'right': False},  # Border control for box plot
        {'top': True, 'bottom': True, 'left': False, 'right': True}    # Border control for violin plot
    ]
)
```
## Customization Options

### Plot Types
You can customize which plots to generate by changing the `subplots_list` parameter:
- `'strip'`: Displays a strip plot.
- `'box'`: Displays a box plot.
- `'violin'`: Displays a half-violin plot.

### Axis Configuration
You can show or hide x and y ticks and labels for each subplot:
- **`show_x`**: List of booleans controlling whether to show x-axis ticks for each plot.
- **`show_y`**: List of booleans controlling whether to show y-axis ticks for each plot.
- **`show_xlabel`, `show_ylabel`**: Lists controlling whether to display x/y-axis labels.

### Titles and Labels
- **`titles`**: A list of strings for the titles of each subplot.
- **`x_labels`, `y_labels`**: Lists of x-axis and y-axis labels for the subplots.

### Custom Palette
Use a custom color palette by passing a list of colors to the `palette` parameter. For example:

```python
palette = ["#1f77b4", "#ff7f0e"]  # Blue and orange colors for the two groups

