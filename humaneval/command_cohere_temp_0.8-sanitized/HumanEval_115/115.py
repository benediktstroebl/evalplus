import math
def max_fill(grid, capacity) :
    wells = len(grid)
    capacity_rows = len(grid[0]) 
    filled_rows = 0 
    filled_volume = 0 
    while filled_rows < wells :
        volume = 0 
        col = 0 
        while col < capacity_rows :
            volume += grid[filled_rows][col] 
            if volume >= capacity :
                filled_volume += (volume // capacity) 
                filled_rows += 1 
                volume %= capacity 
                col = capacity_rows 
            else:
                col += 1 
        if volume > 0 : 
            filled_volume += 1 
    return filled_volume