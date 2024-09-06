import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_rows = sum(1 for row in grid if sum(row) > 0)
    max_fill_rows = math.ceil(filled_rows / capacity)
    
    return max_fill_rows * wells