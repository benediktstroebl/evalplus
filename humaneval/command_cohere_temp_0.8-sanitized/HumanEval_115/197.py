import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    rows = len(grid)

    filled_wells = sum(sum(row) for row in grid)

    if filled_wells <= capacity:
        return filled_wells // capacity
    
    max_fillers = math.ceil(filled_wells / capacity)
    
    filled_rows = (max_fillers * rows) - sum(row[:max_fillers] for row in grid)
    
    return max_fillers - filled_rows // rows
capacity = 1