
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
    # We want to find the minimum number of buckets needed to empty all wells
    # The number of buckets needed to empty all wells is the maximum number of
    # wells that can be emptied with a single bucket
    # We can use dynamic programming to find the maximum number of wells that
    # can be emptied with a single bucket for each row
    # Starting from the bottom row, we can fill buckets by going upwards and
    # rightwards, and we can stop when the bucket capacity is reached or when
    # there are no more wells to fill

    # We can use a binary search to find the maximum number of wells that can
    # be emptied with a single bucket
    # We can start with a large number and then gradually reduce it until we
    # find the maximum number of wells that can be emptied with a single bucket
    # The binary search will terminate when the maximum number of wells that can
    # be emptied with a single bucket is found or when the bucket capacity is reached
    # The maximum number of wells that can be emptied with a single bucket is
    # the
