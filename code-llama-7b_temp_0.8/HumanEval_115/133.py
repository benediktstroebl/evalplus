
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
    # there is no need to use a bucket, you can just remove the water column by column
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    # compute the number of columns
    cols = len(grid[0])
    # compute the number of rows
    rows = len(grid)
    # compute the capacity of the buckets
    cap = capacity
    # compute the number of buckets
    buckets = cols
    # initialize the number of times that the buckets must be lowered
    number_of_times = 0
    # initialize the array of buckets
    buckets_array = []
    # for each bucket
    for bucket in range(0, buckets):
        # append a new bucket to the array of buckets
        buckets_array.append(0)
    # for each column
    for column in range(0, cols):
        # for each row
        for row in range(0, rows):
            # if the current row is zero
            if grid[row][column] == 0:
                # increase the number of times that the buckets must be lowered
                number_of_times += 1
            # otherwise
            else:
                # decrease the water in the bucket by one
                buckets_array[column] -= 1
                # if the bucket is at zero
                if buckets_array[column] <= 0:
                    # add the capacity of the buckets
                    buckets_array[column] += cap
    # return the number of times that the buckets must be lowered
    return number_of_times
