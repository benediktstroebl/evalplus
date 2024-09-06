import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_wells = 0
    filled_units = 0

    for i in range(rows):
        for j in range(wells):
            if grid[i][j] == 1:
                filled_wells += 1
                filled_units += math.floor(j / capacity)

    return filled_wells + max(0, filled_units - capacity)
capacity = 1