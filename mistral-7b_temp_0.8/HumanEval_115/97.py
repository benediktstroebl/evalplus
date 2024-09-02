
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
    m = len(grid[0])

    # We consider the grid to be a 2D array that is [0, n) x [0, m).
    # This is to ensure that we can index into the array without worrying about going out of bounds.
    # So, for example, instead of indexing into the grid at grid[i][j], we can index into it at grid[i-1][j].
    # This is a simple optimization that can be applied to any 2D array, and can save some memory and time.

    # The minimum number of buckets that can be used to empty the wells is at least min(n, m).
    # In order to empty all the wells, we need to fill all the rows and columns.
    # This can be done by taking the minimum of n and m, since we need to fill all the rows and columns.
    # However, the minimum number of buckets that can be used is at least min(n, m).
    # So, we can start with the minimum number of buckets and work our way up from there.
