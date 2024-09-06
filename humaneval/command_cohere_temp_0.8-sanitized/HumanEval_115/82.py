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
                
    return max_rows(filled_rows, capacity) + max_cols(filled_cols, capacity)
def max_rows(filled_rows, capacity):
    return math.ceil(filled_rows / capacity)
def max_cols(filled_cols, capacity):
    return math.ceil(filled_cols / capacity)