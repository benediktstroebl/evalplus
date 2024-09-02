
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

    # Generate the maximum capacity
    max_capacity = grid.size

    # Generate the number of buckets
    num_buckets = grid.shape[0]

    # Create the buckets
    buckets = []
    for i in range(num_buckets):
        buckets.append(max_capacity)

    # Generate the maximum number of operations needed
    max_ops = 0
    for i in range(grid.shape[1]):
        total_water = 0
        for j in range(grid.shape[0]):
            if grid[j][i] == 1:
                total_water += buckets[j]
        max_ops += math.ceil(total_water/capacity)
        for j in range(grid.shape[0]):
            if grid[j][i] == 1:
                buckets[j] -= capacity
            else:
                buckets[j] += capacity

    return max_ops

