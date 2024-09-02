
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
    rows, cols = grid.shape
    capacity_used = grid.copy()
    capacity_used[0][0] = 1
    capacity_used[0][1] = 1
    capacity_used[1][0] = 1
    capacity_used[1][1] = 1
    max_count = 0
    for i in range(2, rows - 1):
        for j in range(2, cols - 1):
            if capacity_used[i][j] == 0:
                capacity_used[i][j] = 1
                max_count = max(max_count, 1)
            else:
                max_count = max(max_count, 1 + capacity_used[i-1][j] + capacity_used[i+1][j-1] + capacity_used[i-1][j-1] + capacity_used[i+1][j])
    return max_count
