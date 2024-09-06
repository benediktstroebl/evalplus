import math
def max_fill(grid, capacity):
    wells = len(grid)
    rows = len(grid[0])
    filled_wells = 0

    for r in range(rows):
        c = 0
        for w in range(wells):
            if grid[w][r] == 1:
                c += 1
                if c == capacity:
                    filled_wells += 1
                    c = 0

    return filled_wells // capacity + (1 if wells % capacity != 0 else 0)