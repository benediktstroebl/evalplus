import math
def max_fill(grid, capacity):
    filled_rows = 0
    filled_cols = 0
    counter = collections.Counter(grid)
    
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '1':
                filled_rows += 1
                filled_cols += 1
            
    if capacity >= filled_rows and capacity >= filled_cols:
        return 0
    
    if filled_rows > filled_cols:
        return max_fill_rows(grid, capacity, filled_rows, filled_cols)
    else:
        return max_fill_cols(grid, capacity, filled_rows, filled_cols)
def max_fill_cols(grid, capacity, filled_rows, filled_cols):
    return capacity * math.ceil(filled_cols / capacity)
def max_fill_rows(grid, capacity, filled_rows, filled_cols):
    return capacity * math.ceil(filled_rows / capacity)