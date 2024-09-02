
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
    # firstly, let's iterate through the array and find the most
    # vertical water column (the height)
    height = max(map(lambda row: sum(row), grid))
    # now we know the most water that can be collected and the height
    # of the water column - but how to collect it?
    # we can calculate the number of full buckets
    full_buckets = math.floor(height / capacity)
    # the number of partial buckets
    partial_buckets = math.ceil(height / capacity) - full_buckets
    # we have two cases: full and partial buckets
    # for full buckets we can use just one bucket
    # for partial we need to get the rest of the water
    # the number of operations is a sum of full and partial
    # with respect to bucket capacity
    return full_buckets * (height - capacity) + partial_buckets * capacity

