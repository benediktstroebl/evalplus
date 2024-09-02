
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
    row, col = len(grid), len(grid[0])

    # 1. Find the largest rectangle we can fill (along the longest dimension)
    #    If this fits our capacity, return the number of times we need to lower the bucket
    #    to fill the rectangle.
    #    If it doesn't, we have to fill it another way.
    #    To do this, we can reduce our grid to only the longest dimension, and then try to
    #    fill the rectangle from the top down

    # 2. If we can't fill the rectangle in the longest dimension, we have to fill it in the
    #    shortest dimension.
    #    This requires a bit of math... We can calculate the area of the rectangle, and then
    #    compute the area of the rectangle with the smallest dimension removed.
    #    The difference between the two is the smallest possible rectangle we can fill.

    # 3. Now we need to calculate the area of the rectangle with the smallest dimension removed.
    #    The easiest way to do this is to remove the smallest dimension, and then repeat the
    #
