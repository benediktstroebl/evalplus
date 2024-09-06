
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
    # Solution
    # Find the number of buckets we need
    num_buckets = math.ceil(capacity)
    # Find the size of the largest well that we can empty with num_buckets
    max_well_size = (num_buckets - 1) * capacity
    # Find the number of wells that are larger than the size of the largest well
    num_large_wells = grid.count(max_well_size)
    # We use num_buckets to empty the wells, but we need num_buckets + 1 to empty the large wells
    return num_buckets + num_large_wells

    # Alternative Solution (BFS)
    # import queue

    # max_bucket_capacity = 0
    # num_buckets = 0

    # while max_bucket_capacity < capacity:
    #     new_max_bucket_capacity = max_bucket_capacity
    #     for i in range(len(grid)):
    #         for j in range(len(grid[i])):
    #            
