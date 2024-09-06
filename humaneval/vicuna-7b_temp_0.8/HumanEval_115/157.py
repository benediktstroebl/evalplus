
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

    def fill_bucket(i, j, k, bucket_capacity):
        if grid[i][j] == 1 and not grid[i][j-1] == 1 and not grid[i-1][j] == 1 and not grid[i-1][j-1] == 1:
            bucket_fill = 0
            while True:
                if bucket_fill + grid[i][j] > bucket_capacity:
                    return
                if not grid[i+bucket_fill][j] == 1:
                    bucket_fill += grid[i][j]
                    grid[i+bucket_fill][j] = 1
                else:
                    return

    def fill_well(i, j, k, bucket_capacity):
        if grid[i][j] == 1:
            bucket_fill = fill_bucket(i, j, k, bucket_capacity)
            grid[i][j] = 0
            grid[i+bucket_fill][j] = 1
            if bucket_fill > 0:
                grid[i][j] = 1
        else:
            fill_well(i-1, j, k, bucket_capacity)
            fill_well(i, j-1, k, bucket_capacity)
            fill_well(i, j+1, k, bucket_capacity)
            fill_well(i+1, j, k, bucket_capacity)

    fill_well(0, 0, 0, bucket_capacity)
