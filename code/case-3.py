import numpy as np
import matplotlib.pyplot as plt

def central_difference(x, y):
    """Computes the central difference derivative for interior points."""
    dy = np.zeros(len(y))
    for i in range(1, len(y) - 1):
        dy[i] = (y[i+1] - y[i-1]) / (x[i+1] - x[i-1])
    return dy[1:-1] # Return only the computed interior points

def integrate_simpsons_trapezoidal(x, y):
    """
    Computes the integral using Simpson's 1/3 Rule for the first 4 intervals 
    and Trapezoidal Rule for the last interval (since n=6 points means 5 intervals).
    """
    h = x[1] - x[0]
    
    # Simpson's 1/3 Rule for points 0 to 4 (x=0 to x=8)
    simpsons_part = (h / 3) * (y[0] + 4*y[1] + 2*y[2] + 4*y[3] + y[4])
    
    # Trapezoidal Rule for points 4 to 5 (x=8 to x=10)
    trapezoidal_part = (h / 2) * (y[4] + y[5])
    
    return simpsons_part + trapezoidal_part

def plot_case(x, y, x_interior, dy, title_y, title_dy, xlabel, ylabel1, ylabel2):
    """Utility function to plot raw data and its derivative side-by-side."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Original Temperature Data
    ax1.plot(x, y, marker='o', color='red', linestyle='-')
    ax1.set_title(title_y)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel1)
    ax1.grid(True)
    
    # Plot 2: Temperature Gradient
    ax2.plot(x_interior, dy, marker='o', color='orange', linestyle='--')
    ax2.set_title(title_dy)
    ax2.set_xlabel(xlabel)
    ax2.set_ylabel(ylabel2)
    ax2.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # ==========================================
    # CASE STUDY 3: Heat Diffusion Data
    # ==========================================
    print("--- CASE STUDY 3: Diffusion Process Simulation ---")
    
    # Given Data
    position_cm = np.array([0, 2, 4, 6, 8, 10])
    temperature_c = np.array([100, 80, 65, 55, 48, 45])

    # 1. Temperature Gradient (Derivative)
    temp_gradient = central_difference(position_cm, temperature_c)
    interior_positions = position_cm[1:-1] # x = 2, 4, 6, 8
    
    # 2. Heat Distribution (Integration)
    total_heat = integrate_simpsons_trapezoidal(position_cm, temperature_c)

    # Output Results
    print(f"Positions (cm) for Gradient: {interior_positions}")
    print(f"Temperature Gradients (°C/cm): {temp_gradient}")
    print("-" * 30)
    print(f"Total Integrated Heat (Simpson's + Trapezoidal): {total_heat:.2f} °C-cm")

    # Visualizations
    plot_case(position_cm, temperature_c, interior_positions, temp_gradient, 
              "Temperature vs Position", "Gradient vs Position", 
              "Position (cm)", "Temperature (°C)", "Gradient (°C/cm)")