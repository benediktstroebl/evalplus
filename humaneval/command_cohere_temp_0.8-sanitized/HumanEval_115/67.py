import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_wells = sum(row for row in grid if any(cell == 1 for cell in row))
    if filled_wells == 0:
        return 0

    return math.ceil(filled_wells / capacity)
capacity = 1