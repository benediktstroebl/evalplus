import math
def max_fill(grid, capacity):
    filled_wells = 0
    for i in range(len(grid)):  
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                filled_wells += 1
        if capacity > filled_wells:
            filled_wells = 0 
        else:
            filled_wells = capacity 
    return max(0, filled_wells)