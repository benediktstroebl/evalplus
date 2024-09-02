
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
    
    num_wells = len(grid)
    bucket_capacity = capacity

    # Define boundaries
    upper_bound = max(grid, key = lambda x : max(x))
    lower_bound = min(grid, key = lambda x : min(x))

    # Initialize buckets
    buckets = [0] * (upper_bound - lower_bound + 1)
    for i in range(num_wells):
        for j in range(num_wells):
            if grid[i][j] == 1:
                buckets[j] += 1

    # Fill wells using buckets
    counter = 0
    while max(buckets)!= 0:
        for i in range(len(buckets)):
            if buckets[i]!= 0:
                if buckets[i] <= bucket_capacity:
                    counter += 1
                    buckets[i] = 0
                else:
                    counter += int(math.ceil(buckets[i] / bucket_capacity))
                    buckets[i] -= bucket_capacity
    return counter
