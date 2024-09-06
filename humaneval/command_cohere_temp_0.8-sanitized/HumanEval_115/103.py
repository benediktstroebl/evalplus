import math
def max_fill(grid, capacity):
    filled_rows = sum(sum(row) for row in grid)
    max_fill_count = math.ceil(filled_rows / capacity)
    return max_fill_count