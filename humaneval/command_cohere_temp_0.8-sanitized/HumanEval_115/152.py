import math
def max_fill(grid, capacity):
    wells = len(grid)
    fills = 0
    for i in range(wells):
        row = grid[i]
        fill_count = 0
        for j in range(len(row)):
            if row[j] == 1:
                fill_count += 1
        fills = max(fills, fill_count)
    return math.ceil(fills / capacity)