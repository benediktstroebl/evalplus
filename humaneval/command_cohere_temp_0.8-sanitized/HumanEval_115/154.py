import math
def max_fill(grid, capacity):
    filled_spots = sum(sum(row) for row in grid)
    spots_per_fill = filled_spots // capacity 
    return spots_per_fill >= 1 and math.ceil(spots_per_fill)