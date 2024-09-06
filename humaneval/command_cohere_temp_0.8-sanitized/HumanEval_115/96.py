import math
def max_fill(grid, capacity) :
    filled_spots = sum(sum(row) for row in grid)
    spots_to_fill = filled_spots % capacity
    return spots_to_fill // capacity if spots_to_fill != 0 else 0