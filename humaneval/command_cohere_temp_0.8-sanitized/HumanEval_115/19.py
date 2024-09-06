import math
def max_fill(grid, capacity):
    wells, rows = len(grid), len(grid[0]) 
    filled_wells = sum(sum(row) for row in grid)
    if filled_wells <= capacity:
        return filled_wells // capacity 
    bucket_fills = math.ceil(filled_wells / capacity)
    return bucket_fills + max(0, rows - bucket_fills)