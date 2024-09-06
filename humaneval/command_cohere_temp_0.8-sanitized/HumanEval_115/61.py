import math
def max_fill(grid, capacity):
    """
    Use buckets to empty the wells.
    """
    rows = len(grid)
    if rows == 0:
        return 0

    cols = len(grid[0])
    if cols == 0:
        return 0

    max_fill = float('-inf')

    def fill_row(row, capacity):
        bucket_falls = 0
        for col in range(cols):
            if row[col] > 0:
                bucket_falls += math.ceil(row[col] / capacity)
                row[col] = 0
        return bucket_falls

    for row in grid:
        current_fill = fill_row(row, capacity)
        if current_fill > max_fill:
            max_fill = current_fill

    return max_fill