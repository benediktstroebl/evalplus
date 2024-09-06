
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
    # Some helpfull data structures:
    # grid[i][j] -> 0 | 1 -> 0 is empty and 1 is a well with water
    #  grid.shape[0] -> no. of rows
    #  grid.shape[1] -> no. of cols
    #  grid.sum() -> no. of wells (is used in bottom_up solution)
    #  max(grid.shape[0], grid.shape[1]) -> no. of wells
    #  math.ceil(val / bucket_capacity) -> no. of buckets needed to empty a well of water (val)
    #  grid.max() -> max no. of units of water in a well
    #  grid.min() -> min no. of units of water in a well
    #  math.gcd(a,b) -> greatest common divisor of two numbers a, b
    #  capacity -> capacity of bucket
    #  grid[i][j] == 0 -> 0th row of ith column
    #  grid[i][j] == 1 -> 0th col of
