import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_rows = sum(1 for row in grid if sum(row) > 0)
    max_fills = math.ceil(filled_rows / capacity)

    extract_count = sum(1 for row in grid if row.count(1) > capacity)
    return max_fills + extract_count