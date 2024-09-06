import math
def max_fill(grid, capacity):
    wells = len(grid)
    buckets = len(grid[0])
    filled_buckets = 0

    for row in grid:
        row_filled_buckets = 0
        for column_filled_buckets in row:
            if column_filled_buckets == 1:
                row_filled_buckets += 1
                filled_buckets += 1

        if row_filled_buckets <= capacity:
            filled_buckets += (buckets - row_filled_buckets) // max(0, capacity - row_filled_buckets)

    return filled_buckets
capacity = 1