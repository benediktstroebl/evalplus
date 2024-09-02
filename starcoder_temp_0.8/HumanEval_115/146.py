
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
    # we can only use one bucket
    # we can have a virtual bucket that can be used to empty the wells
    # we can't reuse a bucket and empty another one
    # we can reuse a bucket and empty another one if the capacity of both buckets is lower than the capacity of the well
    # if the capacity of the well is lower than the capacity of the bucket
    # we can't use the bucket
    # we need to find a way to transfer some of the water from the bucket to the well
    # we can't empty the well directly
    # we need to fill the well indirectly
    # the well must be filled from the bottom up to the top
    # the number of times we need to lower the bucket is the number of empty buckets

    # from the bottom up to the top
    # start from the top right corner
    # transfer water from the bucket to the well
    # the number of times we need to lower the bucket is the number of empty buckets
    # the number of empty buckets is the number of empty wells
    # empty wells must be on the right of the bucket
    # if we move one to the right and keep the bucket on the same well, the number of empty buckets will be the same
    # we can't use the same bucket
    # if we move one to the right and move the bucket to the next well, the number of empty buckets will be increased by 1
    # we can use the next bucket
    # if we move one to the right and move the bucket to the previous well, the number of empty buckets will be increased by 1
    # we can't use the previous bucket
    # the number of empty buckets will be increased by the number of filled buckets
    # the number of filled buckets is the number of non-empty wells
    # the number of non-empty wells is the number of filled buckets + the number of empty wells
    # the number of filled buckets is the number of non-empty wells - the number of empty wells
    # the number of filled buckets is the number of empty wells
    # the number of empty wells is the number of filled buckets
    # the number of empty wells is the number of wells that have water in them
    # the number of empty wells is the number of wells filled by the bucket
    # the number of wells filled by the bucket is the number of filled buckets
    # the number of filled buckets is the number of well
