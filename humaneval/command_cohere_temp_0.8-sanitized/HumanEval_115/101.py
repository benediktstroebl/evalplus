import math
def max_fill(grid, capacity):
    wells = len(grid)
    buckets = len(grid[0])

    filled_buckets = 0

    for row in grid:
        col_filled_buckets = sum(row)
        filled_buckets += math.ceil(col_filled_buckets / capacity)

    return filled_backs + (buckets - wells)  # Add extra buckets for rows