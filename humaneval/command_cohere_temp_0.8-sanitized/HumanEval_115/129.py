import math
def max_fill(grid, capacity):
    wells = len(grid)
    fill_count = 0
    for r in range(wells):
        row = 0
        for c in range(len(grid[r])):
            if grid[r][c] == 1:
                row += 1
                if row > capacity:
                    fill_count += row // capacity
                    row = capacity
            else:
                row = 0
        if row > 0:
            fill_count += row // capacity
    return fill_count