import numpy as np
import matplotlib.pyplot as plt

def central_difference(x, y):
    """Computes the central difference derivative for interior points."""
    dy = np.zeros(len(y))
    for i in range(1, len(y) - 1):
        # Using the exact formula: (P(t+1) - P(t-1)) / (t_next - t_prev)
        dy[i] = (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])
    return dy[1:-1] # Return only the computed interior points

def trapezoidal_rule(x, y):
    """Computes the integral using the Trapezoidal Rule."""
    n = len(x)
    integral = 0
    for i in range(n - 1):
        h = x[i+1] - x[i]
        integral += (h / 2) * (y[i] + y[i+1])
    return integral

def plot_case(x, y, x_interior, dy, title_y, title_dy, xlabel, ylabel1, ylabel2):
    """Utility function to plot raw data and its derivative side-by-side."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Original Data
    ax1.plot(x, y, marker='o', color='b', linestyle='-')
    ax1.set_title(title_y)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel1)
    ax1.grid(True)
    
    # Plot 2: Derivative
    ax2.plot(x_interior, dy, marker='o', color='r', linestyle='--')
    ax2.set_title(title_dy)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel2)
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # ==========================================
    # CASE STUDY 1: Population Growth Data
    # ==========================================
    print("--- CASE STUDY 1: Population Growth ---")
    years = np.array([2020, 2021, 2022, 2023, 2024])
    population = np.array([10000, 10800, 11900, 13200, 14800])

    # Computations
    pop_rate = central_difference(years, population)
    pop_integral = trapezoidal_rule(years, population)
    
    interior_years = years[1:-1]

    # Output Results
    print(f"Years Analyzed for Growth Rate: {interior_years}")
    print(f"Growth Rates (people/yr): {pop_rate}")
    print(f"Total Integrated Population (Trapezoidal): {pop_integral}")

    # Visualizations
    plot_case(years, population, interior_years, pop_rate, 
              "Population vs Time", "Growth Rate vs Time", 
              "Year", "Population", "Growth Rate (people/yr)")