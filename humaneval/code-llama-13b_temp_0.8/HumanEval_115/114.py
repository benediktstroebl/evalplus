
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
    # #Recursive Solution
    # from copy import deepcopy
    # def max_fill(grid, capacity):
    #     global res
    #     n = len(grid)
    #     m = len(grid[0])
    #     if capacity == 0 or capacity < 0:
    #         return 0
    #     if capacity < 1:
    #         return 0
    #     # if all wells are empty, return
    #     if sum(sum(grid, [])) == 0:
    #         return 0

    #     # get maximum row and column index of wells filled
    #     i = n - 1
    #     while i >= 0 and sum(grid[i]) == 0:
    #         i -= 1
    #     i += 1
    #     j = m - 1
    #     while j >= 0 and sum([row[j] for row in grid]) == 0:
    #         j -= 1
    #     j += 1

    #     # if no well is filled, return 0
    #     if i == 0 and j == 0:
    #         return 0

    #     grid1 = deepcopy(grid)
    #     grid2 = deepcopy(grid)
    #     grid3 = deepcopy(grid)
    #     grid4 = deepcopy(grid)
    #     grid1[0][j-1] = 1
    #     grid2[i-1][0] = 1
    #     grid3[i-1][j-1] = 1
    #     grid4[i-1][j-1] = 1

    #     res = min(max_fill(grid1, capacity-1),
    #               max_fill(grid2, capacity-1),
    #               max_fill(grid3, capacity-1),
    #               max_fill(grid4, capacity-1))
    #     return res+1

    # return max_fill(grid, capacity)

    # DP Solution
    from copy import deepcopy
    n = len(grid)
    m = len(grid
