# RC Circuit Simulation - CIT 2118 Lab 2

## Student Information
- **Name:** KEVIN KIPKOECH KEMBOI
- **Reg No:** ENG-219-044/2025
- **Institution:** Multimedia University of Kenya
- **Unit:** Fundamentals of Computers (CIT 2118)
- **Lecturer:** LEC MARTIN

## Project Description
This project simulates the transient response of an RC circuit. It calculates and visualizes the voltage across a 1uF capacitor through a 1k Ohm resistor during both charging and discharging phases.

## Requirements
To run this simulation, you must have Python installed along with the following libraries:
- NumPy
- Matplotlib

You can install these via pip:
`pip install numpy matplotlib`

## How to Run
1. Open your terminal or IDE (like VS Code or PyCharm).
2. Run the script using the command: 
   `python Lab2_RC_Simulation.py`
3. Two graphs will be displayed showing the exponential growth (charging) and decay (discharging) of the voltage.

## Observations
- The time constant (Tau) is 0.001 seconds.
- By 5*Tau (0.005s), the capacitor is effectively fully charged/discharged.
-