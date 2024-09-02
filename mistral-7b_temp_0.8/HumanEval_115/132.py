
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
    # Approach 1: Solution
    # Runtime: 209ms
    # Memory: 39.6MB

    # Corner cases
    if len(grid) == 0:
        return 0

    # 1. initializing variables
    m, n = len(grid), len(grid[0])
    x, y = 0, 0
    res = 0
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # 2. while iterating
    while True:
        x, y = grid[x][y], grid[x][y]
        # stop if there's no water
        if x == 0:
            break

        # 2.1. if capacity is full
        if y == capacity:
            res += 1
            # if the current cell is empty, we don't need to move
            if x == 0:
                break
            # otherwise, we need to move
            else:
                x -= 1

       
