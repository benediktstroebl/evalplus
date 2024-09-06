
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

    grid = [[0] + row + [0] for row in grid] + [[0] * (len(grid[0]) + 2)]
    buckets_count = sum(1 for row in grid for x in row if x == 1)
    buckets_capacity = capacity
    count = 0
    while buckets_count:
        count += 1
        count += max(0, buckets_count - buckets_capacity)
        for i in range(1, len(grid)-1):
            for j in range(1, len(grid[0])-1):
                if grid[i][j] == 1:
                    if sum(grid[i-1][j-1:j+2]) > 0 or sum(grid[i+1][j-1:j+2]) > 0 or sum(grid[i][j-1:j+2]) > 0:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = 1
        buckets_count = sum(1 for row in grid for x in row if x == 1)
    return count

