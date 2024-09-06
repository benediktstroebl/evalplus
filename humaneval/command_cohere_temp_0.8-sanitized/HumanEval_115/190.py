import math
def max_fill(grid, capacity):
    filled_rows = sum(sum(row) for row in grid)
    max_fill_count = filled_rows + math.ceil(math.sqrt(2 * filled_rows)) - 1
    return max_fill_count // capacity + (max_fill_count % capacity > 0)