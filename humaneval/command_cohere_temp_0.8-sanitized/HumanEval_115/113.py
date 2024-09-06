import math
def max_fill(grid, capacity):
    filled_rows = 0
    max_fill_count = 0

    for row in grid:
        filled_rows += row.count(1)

        max_fill_count += math.ceil(filled_rows / capacity)

    return max_fill_count
capacity = 1