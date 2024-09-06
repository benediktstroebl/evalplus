import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    filled_wells = 0
    for row in grid:
        for col in row:
            if col == 1:
                filled_wells += 1
        if filled_wells > capacity:
            return filled_wells // capacity
        filled_wells = 0
    return filled_wells // capacity