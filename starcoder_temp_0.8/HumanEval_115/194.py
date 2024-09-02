
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
    if len(grid) == 0:
        return 0

    # O(nlog(n))
    # for well_idx in range(len(grid)):
    #     # Find the best bucket for each well
    #     best_idx = 0
    #     for idx, bucket in enumerate(grid[well_idx]):
    #         if bucket == 1 and bucket_capacities[idx] > bucket_capacities[best_idx]:
    #             best_idx = idx
    #     bucket_capacities[best_idx] -= 1

    # return sum(bucket_capacities)

    # O(nlog(n))
    # for well_idx in range(len(grid)):
    #     # Find the best bucket for each well
    #     best_idx = 0
    #     for idx, bucket in enumerate(grid[well_idx]):
    #         if bucket == 1 and bucket_capacities[idx] > bucket_capacities[best_idx]:
    #             best_idx = idx
    #     bucket_capacities[best_idx] -= 1

    # return sum(bucket_capacities)

    # O(n)
    # for each_well in grid:
    #     # Find the best bucket for each well
    #     best_idx = 0
    #     for idx, bucket in enumerate(each_well):
    #         if bucket == 1 and bucket_capacities[idx] > bucket_capacities[best_idx]:
    #             best_idx = idx
    #     bucket_capacities[best_idx] -= 1

    # return sum(bucket_capacities)

    # O(n)
    # for each_well in grid:
    #     # Find the best bucket for each well
    #     best_idx = 0
    #     for idx, bucket in enumerate(each_well):
    #         if bucket == 1 and bucket_capacities[idx] > bucket_capacities[best_idx]:
    #             best_idx = idx
    #     bucket_capacities[best_idx] -= 1

    # return sum(bucket_capacities)

    # O(n)
    for each_well in grid:
        # Find the best bucket for each well
        best_idx = 0
        for idx, bucket in enumerate(each_well):
            if bucket == 1
