# =========================================================
# NAME: KEVIN KIPKOECH KEMBOI
# REG NO: ENG-219-044/2025
# UNIT: FUNDAMENTALS OF COMPUTERS (CIT 2118)
# LAB: Lab 2 - RC Circuit Simulation (Charging & Discharging)
# =========================================================

import numpy as np
import matplotlib.pyplot as plt

# 1. Component values as specified in Lab 2
R = 1000      # Resistance in Ohms
C = 1e-6      # Capacitance in Farads (1uF)
V = 5         # Source Voltage in Volts
tau = R * C   # Time Constant (1ms)

# 2. Define Time Range (0 to 10 milliseconds)
t = np.linspace(0, 0.01, 1000)

# 3. Mathematical Formulas
# Charging: Vc(t) = V * (1 - e^(-t/RC))
Vc_charging = V * (1 - np.exp(-t / tau))

# Discharging: Vc(t) = V * e^(-t/RC)
Vc_discharging = V * np.exp(-t / tau)

# 4. Plotting the Results
plt.figure(figsize=(10, 6))

# Plot Charging Curve
plt.subplot(2, 1, 1)
plt.plot(t, Vc_charging, 'b-', label='Charging')
plt.title("Capacitor Charging Curve")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()

# Plot Discharging Curve
plt.subplot(2, 1, 2)
plt.plot(t, Vc_discharging, 'r--', label='Discharging')
plt.title("Capacitor Discharging Curve")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.grid(True)
plt.legend()

plt.tight_layout()
print(f"Simulation Complete. Time Constant (Tau) is: {tau} seconds")
plt.show()