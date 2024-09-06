import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_rows = sum(1 for row in grid if sum(row) > 0)
    max_fill_count = math.ceil(filled_rows / capacity)

    bucket_falls = rows - max_fill_count

    return max_fill_count + bucket_falls
capacity = 1