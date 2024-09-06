import math
def max_fill(grid, capacity):
    wells = len(grid)
    rows = len(grid[0])
    filled_wells = 0
    
    for i in range(wells):
        for j in range(rows):
            if grid[i][j] == 1:
                filled_wells += math.ceil(j / capacity)
    
    return filled_wells
capacity = 1