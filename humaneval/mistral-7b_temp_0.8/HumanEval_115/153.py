
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

    # a backtracking solution is possible
    # but we use dynamic programming instead

    # our grid will be m x n.
    # we can use a 1-dimensional array to store the grid:
    # a[i] represents the state of the grid at row i
    # for example, a[0] = 010110111 represents the first 10 columns of the grid
    # a[1] = 1000011011 represents the next 10 columns, and so on

    # at any point in time, we know the state of the grid a[i] for all i up to and including the current row
    # we can use this to calculate the state of the grid for the next row
    # the number of steps required to empty the wells is simply the number of rows in the grid

    # each well can be emptied using a single bucket
    # so to calculate the state of the grid for the next row, we simply iterate over the current row
    # and fill each well that has 1 in it using the current bucket capacity
    # for
