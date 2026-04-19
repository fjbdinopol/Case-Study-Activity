import numpy as np
import matplotlib.pyplot as plt

def central_difference(x, y):
    """Computes the central difference derivative for interior points."""
    dy = np.zeros(len(y))
    for i in range(1, len(y) - 1):
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
    
    # Plot 1: Original Volume Data
    ax1.plot(x, y, marker='o', color='cyan', linestyle='-')
    ax1.set_title(title_y)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel1)
    ax1.grid(True)
    
    # Plot 2: Flow Rate
    ax2.plot(x_interior, dy, marker='o', color='blue', linestyle='--')
    ax2.set_title(title_dy)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel2)
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # ==========================================
    # CASE STUDY 4: Water Tank Filling Rate
    # ==========================================
    print("--- CASE STUDY 4: Water Tank Filling Rate Analysis ---")
    
    # Given Data
    time_mins = np.array([0, 2, 4, 6, 8, 10])
    volume_l = np.array([0, 40, 110, 210, 340, 500])

    # 1. Flow Rate Estimation (Derivative of Volume)
    flow_rate = central_difference(time_mins, volume_l)
    interior_time = time_mins[1:-1] # t = 2, 4, 6, 8
    
    # 2. Total Volume Accumulated (Integration)
    total_volume_integral = trapezoidal_rule(time_mins, volume_l)

    # Output Results
    print(f"Time (min) for Flow Rate: {interior_time}")
    print(f"Estimated Flow Rate (L/min): {flow_rate}")
    print("-" * 30)
    print(f"Total Integrated Volume (Trapezoidal): {total_volume_integral:.2f} L-min")

    # Visualizations
    plot_case(time_mins, volume_l, interior_time, flow_rate, 
              "Volume vs Time", "Flow Rate vs Time", 
              "Time (min)", "Volume (L)", "Flow Rate (L/min)")