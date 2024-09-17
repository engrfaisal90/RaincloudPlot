import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import ptitprince as pt  # For half violin plots

class RainCloudPlot:
    def __init__(self, data, jitter_strength=0.03, palette="Set2"):
        """
        Initialize the ComparativePlot class with data, jitter strength, and default color palette.
        
        Parameters:
        - data: A pandas DataFrame with two columns (e.g., "Group 1" and "Group 2").
        - jitter_strength: Strength of jitter for strip plot.
        - palette: Default color palette for the plots (default is "Set2").
        """
        self.data = data
        self.jitter_strength = jitter_strength
        self.palette = sns.color_palette(palette)

    def generate_plot(self, subplots_list, 
                      show_x=None, show_y=None, 
                      show_xlabel=None, show_ylabel=None, 
                      titles=None, x_labels=None, y_labels=None, 
                      palette=None, show_border=None):
        """
        Generate plots based on the subplots_list provided, axis visibility, titles, axis labels, border control, and custom color palette.
        """
        num_plots = len(subplots_list)
        fig, axes = plt.subplots(1, num_plots, figsize=(4 * num_plots, 4), gridspec_kw={'width_ratios': [1] * num_plots})

        if num_plots == 1:
            axes = [axes]  # Ensure axes is always iterable
        
        # Set default values
        titles = titles or [''] * num_plots
        x_labels = x_labels or [''] * num_plots
        y_labels = y_labels or [''] * num_plots
        show_x = show_x or [True] * num_plots
        show_y = show_y or [True] * num_plots
        show_xlabel = show_xlabel or [True] * num_plots
        show_ylabel = show_ylabel or [True] * num_plots
        show_border = show_border or [{'top': True, 'bottom': True, 'left': True, 'right': True}] * num_plots
        palette = palette or self.palette
        group1_color, group2_color = palette[0], palette[1]

        # Loop through subplots
        for i, plot_type in enumerate(subplots_list):
            ax = axes[i]
            if plot_type == 'strip':
                self._strip_plot(ax, i, titles, x_labels, y_labels, show_x, show_y, show_xlabel, show_ylabel, palette, show_border)
            elif plot_type == 'box':
                self._box_plot(ax, i, titles, x_labels, y_labels, show_x, show_y, show_xlabel, show_ylabel, palette, show_border)
            elif plot_type == 'violin':
                self._half_violin_plot(ax, i, titles, x_labels, y_labels, show_x, show_y, show_xlabel, show_ylabel, group1_color, group2_color, show_border)

        # Adjust layout to remove spacing between subplots
        plt.subplots_adjust(wspace=0, hspace=0)
        plt.tight_layout()
        plt.show()

    def _set_labels_and_ticks(self, ax, i, x_labels, y_labels, show_x, show_y, show_xlabel, show_ylabel):
        """Helper function to set axis labels and ticks."""
        ax.set_xlabel(x_labels[i] if show_xlabel[i] else "")
        ax.set_ylabel(y_labels[i] if show_ylabel[i] else "")
        if not show_x[i]:
            ax.set_xticklabels([])  # Remove the x-tick labels
            ax.tick_params(bottom=False)  # Remove the x-tick marks
        if not show_y[i]:
            ax.set_yticklabels([])  # Remove the y-tick labels
            ax.tick_params(left=False)  # Remove the y-tick marks

    def _set_borders(self, ax, show_border):
        """Helper function to control border visibility."""
        ax.spines['top'].set_visible(show_border['top'])
        ax.spines['bottom'].set_visible(show_border['bottom'])
        ax.spines['left'].set_visible(show_border['left'])
        ax.spines['right'].set_visible(show_border['right'])

    def _strip_plot(self, ax, i, titles, x_labels, y_labels, show_x, show_y, show_xlabel, show_ylabel, palette, show_border):
        """Generate a strip plot."""
        group1_jittered_x = np.random.normal(0, self.jitter_strength, size=len(self.data))
        group2_jittered_x = np.random.normal(1, self.jitter_strength, size=len(self.data))

        df_jittered = pd.DataFrame({
            'Jittered_x': np.concatenate([group1_jittered_x, group2_jittered_x]),
            'Values': np.concatenate([self.data.iloc[:, 0], self.data.iloc[:, 1]]),
            'Group': ['Group 1'] * len(self.data) + ['Group 2'] * len(self.data)
        })

        for j in range(self.data.shape[0]):
            ax.plot([group1_jittered_x[j], group2_jittered_x[j]], 
                    [self.data.iloc[j, 0], self.data.iloc[j, 1]], color='gray', lw=1)

        sns.scatterplot(x='Jittered_x', y='Values', hue='Group', data=df_jittered, palette=palette[:2], s=100, edgecolor="white", ax=ax)
        ax.legend(title="Group", loc="upper left")
        ax.set_title(titles[i])
        
        # Set labels and borders
        self._set_labels_and_ticks(ax, i, x_labels, y_labels, show_x, show_y, show_xlabel, show_ylabel)
        self._set_borders(ax, show_border[i])

    def _box_plot(self, ax, i, titles, x_labels, y_labels, show_x, show_y, show_xlabel, show_ylabel, palette, show_border):
        """Generate a box plot."""
        sns.boxplot(data=[self.data.iloc[:, 0], self.data.iloc[:, 1]], ax=ax, width=0.4, palette=palette[:2])
        ax.set_xticklabels(["Group 1", "Group 2"])
        ax.set_title(titles[i])
        
        # Set labels and borders
        self._set_labels_and_ticks(ax, i, x_labels, y_labels, show_x, show_y, show_xlabel, show_ylabel)
        self._set_borders(ax, show_border[i])

    def _half_violin_plot(self, ax, i, titles, x_labels, y_labels, show_x, show_y, show_xlabel, show_ylabel, group1_color, group2_color, show_border):
        """Generate a half violin plot."""
        pt.half_violinplot(x=np.repeat(0, len(self.data)), y=self.data.iloc[:, 0], palette=[group1_color], bw=0.3, scale="area", width=0.6, inner=None, ax=ax)
        pt.half_violinplot(x=np.repeat(0, len(self.data)), y=self.data.iloc[:, 1], palette=[group2_color], bw=0.3, scale="area", width=0.6, inner=None, ax=ax, alpha=0.8)
        ax.set_title(titles[i])

        # Set labels and borders
        self._set_labels_and_ticks(ax, i, x_labels, y_labels, show_x, show_y, show_xlabel, show_ylabel)
        self._set_borders(ax, show_border[i])
        ax.set_xlim(-0.5, -0.13)

# Usage example:
np.random.seed(42)
df = pd.DataFrame({
    "Group 1": np.random.normal(3, 0.5, 20),
    "Group 2": np.random.normal(4, 0.5, 20)
})

custom_palette = sns.color_palette("coolwarm", 2)

plotter = RainCloudPlot(data=df, jitter_strength=0.05)

# Define the borders for each plot
border_control = [
    {'top': True, 'bottom': True, 'left': True, 'right': False},  # First subplot borders
    {'top': True, 'bottom': True, 'left': False, 'right': False},  # Second subplot borders
    {'top': True, 'bottom': True, 'left': False, 'right': True}    # Third subplot borders
]

# Generate plots with custom settings for each subplot
plotter.generate_plot(
    ['strip', 'box', 'violin'], 
    show_x=[False, False, True], 
    show_y=[False, False, False], 
    show_xlabel=[False, False, False], 
    show_ylabel=[False, False, False], 
    titles=["Strip Plot", "Box Plot", "Violin Plot"],
    x_labels=["X-axis Label 1", "X-axis Label 2", "X-axis Label 3"],
    y_labels=["Y-axis Label 1", "Y-axis Label 2", "Y-axis Label 3"],
    palette=custom_palette,
    show_border=border_control
)
