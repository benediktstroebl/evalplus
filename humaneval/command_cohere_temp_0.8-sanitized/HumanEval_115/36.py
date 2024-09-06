import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    max_fill = 0

    for row in grid:
        curr_fill = 0
        for val in row:
            if val == 1:
                curr_fill += 1
            else:
                curr_fill = 0
            max_fill = max(max_fill, curr_fill)

    return max_fill // capacity + math.ceil(max_fill % capacity / capacity)