import math
def max_fill(grid, capacity):
    filled_rows = 0
    max_fillings = 0

    for row in grid:
        filled_rows += row.count(1)

        max_fillings = max(
            max_fillings,
            math.ceil(filled_rows / capacity)
        )

    return max_fillings