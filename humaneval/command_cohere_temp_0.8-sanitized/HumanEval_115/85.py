import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_wells = 0
    max_filled = 0

    for row in grid:
        filled_wells += sum(row)

        curr_filled = math.ceil(filled_wells / capacity)
        max_filled = max(max_filled, curr_filled)

    return max_filled