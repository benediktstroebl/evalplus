
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
    # brute force, TLE
    # n_wells = len(grid)
    # n_buckets = n_wells * len(grid[0])
    # g = [[0]*n_buckets for _ in range(n_wells)]
    # max_units = 0
    # for i in range(n_wells):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == 1:
    #             if j > max_units:
    #                 max_units = j
    #             g[i][j+max_units] = 1
    # count = 0
    # while True:
    #     f = True
    #     for i in range(n_wells):
    #         for j in range(max_units):
    #             if g[i][j] == 1 and g[i][j+1] == 0:
    #                 g[i][j] = 0
    #                 g[i][j+1] = 1
    #                 f = False
    #                 count += 1
    #     if f:
    #         break
    # return count

    # dp
    n_wells = len(grid)
    n_buckets = n_wells * len(grid[0])
    dp = [[0]*n_buckets for _ in range(n_wells)]
    max_units = 0
    for i in range(n_wells):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                if j > max_units:
                    max_units = j
                dp[i][j+max_units] = 1
    count = 0
    for i in range(n_wells):
        for j in range(max_units):
            if dp[i][j] == 1:
                if j == max_units-1:
                    dp[i][j] = 0
                    dp[i][j+1] = 1
                elif dp[i][j+1] == 0:
                    dp[i][j] = 0
                    dp[i][j+1] = 1
                    count += 1
    return count


