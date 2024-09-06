import math
def max_fill(grid, capacity):
    wells = len(grid)
    max_fill = 0

    for i in range(wells):
        row = 0
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                row += 1
                if row > capacity:
                    max_fill = max(max_fill, row)
                    row = 0
            else:
                if row > 0:
                    max_fill = max(max_fill, row)
                    row = 0

    if row > 0:
        max_fill = max(max_fill, row)

    return max_fill