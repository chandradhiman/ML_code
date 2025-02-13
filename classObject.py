import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class DataPlotter:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None

    def load_data(self):
        """Load data from CSV file and convert class labels."""
        cols = ["fLength", "fwidth", "fSize", "fconc1", "fasym", 
                "f3Long", "fM3Trans", "falpha", "fdist", "class"]
        
        self.df = pd.read_csv(self.filepath, names=cols)
        print(self.df.head())

        # Before conversion
        print("Before conversion:", self.df["class"].unique())

        # Convert "g" to 1 and other classes to 0
        self.df["class"] = (self.df["class"] == "g").astype(int)

        # After conversion
        print("After conversion:", self.df["class"].unique())

    def plot_histograms(self):
        """Plot histograms for each feature separately for class 1."""
        if self.df is None:
            print("Data not loaded. Run load_data() first.")
            return

        cols = self.df.columns  # Exclude 'class' column
        print("Columns to plot:", cols)

        for label in cols:
            plt.figure(figsize=(6, 4))
            plt.hist(self.df[self.df["class"] == 1][label], 
                     color='blue', label=label, alpha=0.7, density=True)

            plt.title(f"Histogram of {label}")
            plt.xlabel(label)
            plt.ylabel("Probability")
            plt.legend()
            plt.show()

# Usage:
plotter = DataPlotter("./magic04.data")