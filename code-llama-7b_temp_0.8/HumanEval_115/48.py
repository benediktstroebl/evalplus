
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
    # Your code here
    # how many times we need to move the buckets to the wells
    # referred to as the number of extractions
    # no need to use a bucket to extract water from a well that is already empty
    # since we are looking for the minimum number of extractions
    # the empty wells are the ones where the sum of all buckets in each row is equal to 0
    # here we start at the top left and look at each column of each row
    # if we find that a column is empty, we move the buckets to the first non-empty well in that row
    # this process repeats until all wells are empty
    # we return the number of extractions
    # we make use of the math library to find the absolute value of the number of extractions
    # the number of extractions will be negative if we first move the buckets to the first non-empty well in each row
    # then we move the buckets to the next non-empty well in each row
    # the absolute value of a negative number is the same as the positive value of that number minus 1
    # e.g. the absolute value of -5 is the same as -5 + 1 = -4
    # the absolute value of -1 is the same as -1 + 1 = 0
    # the absolute value of 0 is the same as 0 + 1 = 1
    # the absolute value of 1 is the same as 1 + 1 = 2
    # the absolute value of 4 is the same as 4 + 1 = 5

    import numpy as np

    # convert the 2D list into a 2D numpy array
    grid = np.array(grid)
    # get the number of rows
    num_rows = np.shape(grid)[0]
    # get the number of columns
    num_cols = np.shape(grid)[1]
    # get the number of buckets
    num_buckets = num_rows * capacity
    # set a variable to keep track of the number of extractions
    extractions = 0
    # create a variable to keep track of whether we are moving the buckets down or up
    # initially we move the buckets down
    
