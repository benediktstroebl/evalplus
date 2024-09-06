
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

    # To find maximum area, we need to find the contours of the grid, i.e, 
    # we need to find all the (x,y) co-ordinates where we have 1 in the grid.
    # And after finding the contours, we need to check whether the water level is
    # less than the capacity of the bucket. If so, we need to fill the contour.
    # So, we need to iterate through the grid and check each cell whether 1 or not.
    # If 1 is present, then we need to add it to the contour list.
    # After finding the contour list, we need to check the water level at each 
    # (x,y) in the contour. To do this, we need to subtract the x,y co-ordinates
    # from the (0,0) point in the grid.
    # If the water level is less than the capacity of the bucket, we need to
    # fill the bucket with water.
    # So, we need to iterate through the contour list and check the water level
    # at each point.
