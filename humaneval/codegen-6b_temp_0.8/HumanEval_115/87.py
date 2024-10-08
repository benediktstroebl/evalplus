
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
    n = len(grid)
    bucket_num = [[0] * (capacity+1) for i in range(n)]
    bucket_num[0][0] = grid[0][0]
    for i in range(1,n):
        bucket_num[i][0] = grid[i][0] + bucket_num[i-1][0]
    for j in range(1,capacity+1):
        bucket_num[0][j] = grid[0][j] + bucket_num[0][j-1]
    for i in range(1,n):
        for j in range(1,capacity+1):
            print(bucket_num[i-1][j-1], grid[i][j])
            bucket_num[i][j] = grid[i][j] + max(bucket_num[i-1][j], bucket_num[i][j-1])
    return bucket_num[n-1][capacity]
  
    
