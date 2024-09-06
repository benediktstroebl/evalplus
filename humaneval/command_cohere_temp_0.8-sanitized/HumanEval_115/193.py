import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    buckets = len(grid)

    filled_buckets = 0
    empty_wells = 0

    for well in range(wells):
        row = [0] * buckets
        for bucket in range(buckets):
            row[bucket] = grid[bucket][well]
        filled_buckets += row.count(1)
        empty_wells += row.count(0)

    return max(empty_wells, filled_buckets - 1) // capacity + 1
capacity = 1