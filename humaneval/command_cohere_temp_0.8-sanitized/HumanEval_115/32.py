import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_wells = 0

    for i in range(rows):
        row = grid[i]
        for j in range(wells):
            if row[j] == 1:
                filled_wells += 1
                if filled_wells == capacity:
                    return filled_wells
    
    return filled_wells