
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

    buckets = [capacity for _ in range(len(grid))]
    buckets_max = math.ceil(len(grid) / capacity)
    buckets_min = math.floor(len(grid) / capacity)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if j > 0 and grid[i][j-1] == 1:
                    buckets[i] = max(buckets[i], buckets[i-1] + 1)
                if j < len(grid[i]) - 1 and grid[i][j+1] == 1:
                    buckets[i] = max(buckets[i], buckets[i-1] + 1)
                if i > 0 and grid[i-1][j] == 1:
                    buckets[i] = max(buckets[i], buckets[i-1] + 1)
                if i < len(grid) - 1 and grid[i+1][j] == 1:
                    buckets[i] = max
