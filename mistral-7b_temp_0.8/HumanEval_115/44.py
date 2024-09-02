
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
    # todo: need to remember if bucket can fill or not
    # todo: consider multiple bucket and return total number of move
    # todo: consider resize capacity
    # todo: consider water can be moved from one well to another
    # todo: consider water can be moved from one well to another if wells are adjacent
    # todo: consider water can be moved from one well to another if wells are not adjacent but the line between them is full of water

    if capacity == 1:
        if grid[0] == [0] * len(grid[0]):
            return 0
        return max(len(grid) - 1, len(grid[0]) - 1)

    n, m = len(grid), len(grid[0])
    grid = [[math.inf if i == 0 else 0 for i in range(m)] for i in range(n)]
    grid[0][0] = grid[0][m-1] = grid[n-1][m-1] = grid[n-1][0] = 0
    queue = [(0, 0)]
