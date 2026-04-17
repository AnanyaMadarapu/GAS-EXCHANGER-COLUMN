import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# INPUT PARAMETERS
# -----------------------------
N = 10                 # number of trays
y_in = 0.15            # inlet CO2 mole fraction (gas)
m = 1.2                # equilibrium constant (y = m*x)
removal_factor = 0.85  # fraction remaining after each stage

# -----------------------------
# INITIALIZE
# -----------------------------
y = [y_in]   # gas phase
x = [0]      # liquid phase

# -----------------------------
# STAGE-WISE CALCULATION
# -----------------------------
for i in range(N):
    # equilibrium relation
    x_i = y[-1] / m
    x.append(x_i)
    
    # absorption step
    y_next = y[-1] * removal_factor
    y.append(y_next)

# -----------------------------
# RESULTS
# -----------------------------
stages = np.arange(0, N+1)

plt.figure()
plt.plot(stages, y, marker='o', label="Gas phase (y)")
plt.plot(stages, x, marker='s', label="Liquid phase (x)")
plt.xlabel("Stage Number")
plt.ylabel("Mole Fraction")
plt.title("CO₂ Absorption in Amine Tray Column")
plt.legend()
plt.grid()
plt.show()

# Efficiency
efficiency = (y_in - y[-1]) / y_in * 100
print(f"Final CO2 mole fraction: {y[-1]:.4f}")
print(f"CO2 Removal Efficiency: {efficiency:.2f}%")