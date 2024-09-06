
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
    m = len(grid)
    n = len(grid[0])
    capacity = int(capacity)
    
    def find_empty_water(grid, x, y, capacity):
        if grid[x][y] == 1:
            return 0
        if grid[x][y] == 0:
            return capacity
        grid[x][y] = 2
        
        left = find_empty_water(grid, x, y-1, capacity)
        right = find_empty_water(grid, x, y+1, capacity)
        up = find_empty_water(grid, x-1, y, capacity)
        down = find_empty_water(grid, x+1, y, capacity)
        
        if left < right:
            return left
        else:
            return right
    
    def find_empty_bucket(grid, i, j):
        if grid[i][j] != 0:
            return 0
        else:
            grid[i][j] = 3
            return 1
    
    def find_water(grid, x, y, capacity):
        if grid[x][y] == 1:
            return 0
        if grid[x][y] == 2:
            return capacity
        grid[x][y] = 4
        
        left = find_water(grid, x, y-1, capacity)
        right = find_water(grid, x, y+1, capacity)
        up = find_water(grid, x-1, y, capacity)
        down = find_water(grid, x+1, y, capacity)
        
        if left < right:
            return left
        else:
            return right
    
    def move_bucket(grid, x, y):
        if grid[x][y] == 2 or grid[x][y] == 4:
            return grid
        
        grid[x][y] = 3
        water = find_water(grid, x, y, capacity)
        if water == 0:
            return grid
        
        empty_water = find_empty_water(grid, x, y, capacity)
