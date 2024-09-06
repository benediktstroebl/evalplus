import math
def max_fill(grid, capacity):
    """
    Compute the maximum water that can be fetched 
    from a grid of wells with a given capacity.
    """
    if not capacity:
        return 0
    
    # Calculate maximum water from rows and columns
    row_max = max_fill_row(grid, capacity)
    col_max = max_fill_col(grid, capacity)
    
    # Return maximum of calculations
    return max(row_max, col_max)
def max_fill_row(grid, capacity):
    """
    Compute the maximum water from a single row.
    """
    if not grid:
        return 0
    
    row = len(grid)
    max_fill = 0
    
    for col in range(len(grid[0])):
        count = 0
        for i in range(row):
            if grid[i][col] == 1:
                count += 1
                if count > capacity: 
                    return 0 
        max_fill = max(max_fill, count)
    
    return max_fill
def max_fill_col(grid, capacity):
    """
    Compute the maximum water from a single column.
    """
    if not grid:
        return 0
    
    col = len(grid[0])
    max_fill = 0
    
    for row in range(len(grid)):
        count = 0
        for j in range(col):
            if grid[row][j] == 1:
                count += 1
                if count > capacity: 
                    return 0 
        max_fill = max(max_fill, count)
    
    return max_fill
capacity = 1