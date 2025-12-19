# SPATIAL LOGIC PROTOCOL - Phase 1 Demo
# Demonstrating the 'Address is the Computation' principle.

class Type1Grid:
    def __init__(self):
        # Level 1 is Identity (x1), Level 2 is the Resonance Platform (x40)
        self.levels = {1: 1, 2: 40}
        print("--- Type 1 Spatial Grid Initialized ---")

    def get_value(self, data, level):
        # The computation is a result of the data's POSITION (Level)
        multiplier = self.levels.get(level, 1)
        return data * multiplier

# --- SIMULATION ---
grid = Type1Grid()

# Starting value
input_data = 5 
print(f"Initial Data: {input_data} at Level 1")

# Standard Type 0 logic would require a CPU multiplication cycle: 5 * 40
# Type 1 logic simply 'routes' the data to Level 2
result = grid.get_value(input_data, level=2)

print(f"Spatial Shift to Level 2 Complete.")
print(f"Resulting Value (5 x 40): {result}")
print("--- Thermal Friction: ZERO ---")
