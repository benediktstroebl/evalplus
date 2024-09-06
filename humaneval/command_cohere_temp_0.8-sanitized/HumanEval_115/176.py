import math
def max_fill(grid, capacity):
    filled_rows = sum(sum(row) for row in grid)
    max_fills = filled_rows + math.ceil(math.sqrt(filled_rows))
    
    return max_fills // capacity
capacity = 1