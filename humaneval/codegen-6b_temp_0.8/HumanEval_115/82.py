
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
    """
    My idea here is to use dynamic programming to find the number of times you need to lower buckets.
    To do that, I will rewrite this problem as optimal to 1. Given two points of rain falling to each well,
    then the number of times you need to lower buckets is the max between the two,
    or the resulting number of times you need to lower buckets from two buckets that were above the water,
    assuming you can lower both buckets simultaneously.
    """
    # rows, cols = len(grid), len(grid[0])
    # num_wells = rows * cols
    # dp = [[0 for _ in range(num_wells)] for _ in range(num_wells)]

    # for i in range(rows):
    #     for j in range(cols):
    #         # top_left, top_right = (i,j), (i,j)
    #         # bottom_left, bottom_right = (i,j), (i,j)
    #         # first_fill = max(0, min(grid[top_left[0]][top_left[1]], grid[top_right[0]][top_right[1]]) - grid[i][j])
    #         # second_fill = max(0, min(grid[bottom_left[0]][bottom_left[1]], grid[bottom_right[0]][bottom_right[1]]) - grid[i][j])
    #         # water_list = [first_fill, second_fill]
    #         # for k in range(2):
    #         #     if water_list[k] > 0:
    #         #         dp[top_left][bottom_left] = max(dp[top_left][bottom_left], water_list[k])
    #         #         dp[top_right][bottom_right] = max(dp[top_right][bottom_right], water_list[k])
    #         #         dp[top_left][top_right] = max(dp[top_left][top_right], water_list[k] + dp[bottom_left][bottom_right])
    #         #         dp[bottom_left