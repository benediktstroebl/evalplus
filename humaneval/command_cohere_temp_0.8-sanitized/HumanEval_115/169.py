import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    buckets = len(grid)
    filled_buckets = 0

    for row in grid:
        col_filled_buckets = 0
        for col in row:
            if col == 1:
                col_filled_buckets += 1
            else:
                filled_buckets = max(filled_buckets, col_filled_buckets)
        if row[wells - 1] == 1:
            filled_buckets += 1

    return math.ceil(filled_buckets / capacity)