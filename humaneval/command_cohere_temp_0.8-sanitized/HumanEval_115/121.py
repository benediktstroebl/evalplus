import math
def max_fill(grid, capacity) :
    filled_spots = sum(sum(row) for row in grid)
    return math.ceil(filled_spots / capacity)