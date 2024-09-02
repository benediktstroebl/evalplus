
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
    def dfs(row, grid, bucket_fill):
        if row < 0 or row >= grid.length or grid[row][grid[row].find('1')] < 0:
            return
        
        for col in range(grid[row].find('1')+1, grid[row].find('0')+1):
            if grid[row][col] == 0:
                bucket_fill = 0
                grid[row][col] = 1
                dfs(row+1, grid, bucket_fill)
                grid[row][col] = 0
                bucket_fill = max(bucket_fill, grid[row][col])
        
    bucket_fill = max_fill(grid, 1)
    for row in range(1, grid.find('1')+1):
        grid[row][grid[row].find('1')] = 0
    return bucket_fill
