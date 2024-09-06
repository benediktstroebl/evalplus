import math
def max_fill(grid, capacity):
    wells = len(grid)
    trips = 0
    for well in range(wells):
        row = 0
        for col in range(len(grid[well])):
            if grid[well][col] == 1:
                row += math.ceil(row + col + 1 / capacity)
        trips = max(trips, row)
    return trips
capacity = 1