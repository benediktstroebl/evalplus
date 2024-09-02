
def max_fill(grid, capacity):
    import math
    """
    You are given a rectangular grid of wells. Each row represents a single well,
    and each 1 in a row represents a single unit of water.
    Each well has a corresponding bucket that can be used to extract water from it, 
    and all buckets have the same capacity.
    Your task is to use the buckets to empty the wells.
    Output the number of times you need to lower the buckets.

    Example 1:
        Input: 
            grid : [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
            bucket_capacity : 1
        Output: 6

    Example 2:
        Input: 
            grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
            bucket_capacity : 2
        Output: 5
    
    Example 3:
        Input: 
            grid : [[0,0,0], [0,0,0]]
            bucket_capacity : 5
        Output: 0

    Constraints:
        * all wells have the same length
        * 1 <= grid.length <= 10^2
        * 1 <= grid[:,1].length <= 10^2
        * grid[i][j] -> 0 | 1
        * 1 <= capacity <= 10
    """
    num_row, num_col = len(grid), len(grid[0])
    for row in range(num_row):
        items = []
        for col in range(num_col):
            if grid[row][col] == 1:
                items.append((col, col, row, row))
                
        items.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
        
        for i in range(len(items)-1):
            item = items[i]
            if item[2] == items[i+1][2] and item[3] == items[i+1][3]:
                continue
            
            water_from = min(item[1], capacity-item[0])
            
            if water_from == capacity-item[0]:
                capacity -= item[0]
                grid[item[2]][item[3]] = 0
            else:
                capacity -= water_from
                grid[item[2]][item[3]] -= water_from 

    return sum([1 if any(x) else 0 for x in grid])
