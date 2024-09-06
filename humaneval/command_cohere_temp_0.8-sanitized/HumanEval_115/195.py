import math
def max_fill(grid, capacity):
    wells = len(grid)
    rows = len(grid[0])
    filled_wells = 0

    for i in range(wells):
        row = 0
        for j in range(rows):
            if grid[i][j] == 1:
                row += 1
                if row <= capacity:
                    filled_wells += row
                else:
                    filled_wells += row // capacity * capacity
                    row = capacity
            else:
                row = 0
        
        if row > 0:
            filled_wells += row // capacity if row % capacity != 0 else row // capacity + 1
            
    return filled_wells
capacity = 1