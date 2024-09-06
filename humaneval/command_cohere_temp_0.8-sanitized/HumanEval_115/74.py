import math
def max_fill(grid, capacity):
    wells = len(grid[0])
    filled_wells = 0
    buckets = 0
    
    for row in grid:
        row_filled_wells = 0
        for col in row:
            if col == 1:
                row_filled_wells += 1
                filled_wells += 1
            else:
                row_filled_wells = 0
                
        if row_filled_wells > capacity:
            return -1
        
        buckets += row_filled_wells // capacity
        
        if row_filled_wells % capacity != 0:
            buckets += 1
                
    return buckets * filled_wells