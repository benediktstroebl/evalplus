
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
    # raise NotImplementedError("You need to code this one!")

    #TODO: how do we know the initial number of buckets to use?
    # 1. CAN WE SOLVE THIS WITHOUT A SORT?
    # yes! we can just use 1 bucket
    # how do we know which bucket to use?
    # we can just use the smallest bucket possible to get the largest number of units possible
    # 2. HOW DO WE KNOW WHEN TO ADD ANOTHER BUCKET?
    # is it when we have less than the capacity left in the bucket? 
    # if we run out of units, we can't just use the bucket 
    # so we need to add another bucket if we run out
    
    # we can add as many buckets as we need to get the largest number of units
    # how do we know when to stop? 
    # we know when we have no more units to extract from the wells
    # if we get to a point where we can't extract any more units, we can stop
    # how do we know when we can't extract any more units?
    # is it when we can't get any water out of the wells?
    # can we get any water out of the wells?
    # it depends on the wells
    # is there any 1s left in the grid?
    # how do we know if there is 1s left in the grid?
    # if we can find a 1 in the grid, we know we can still get water
    # so we need to check if there is a 1 in the grid, and if there is not, we know we can stop

    # so we need to check if there is a 1 in the grid, and if there is not, we know we can stop
    # to check if there is a 1 in the grid, we need to search for a 1 in the grid
    # if we search the grid, we can't use another bucket because we need to check the grid for 1s
    # we need to check the grid one row at a time
    # to check the grid, we need to check one row of the grid at a time
    
