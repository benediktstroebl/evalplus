
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
    # #Initial thoughts
    # first_thoughts = []
    # for row in grid:
    #     for unit in row:
    #         first_thoughts.append(unit)
    # first_thoughts = sorted(first_thoughts, reverse=True)
    # bucket_capacity = min(bucket_capacity, len(first_thoughts))
    # for i in range(bucket_capacity):
    #     first_thoughts[i] = 0
    # return sum(first_thoughts)

    # Optimal solution
    # import math
    # import numpy as np
    # n_rows = len(grid)
    # n_cols = len(grid[0])
    # grid = np.array(grid)
    # for i in range(n_rows):
    #     for j in range(n_cols):
    #         if grid[i][j] >= capacity:
    #             grid[i][j] = capacity
    # return math.prod(grid.shape) - np.count_nonzero(grid)

    #Solution
    total_units = 0
    for row in grid:
        total_units += sum(row)
    bucket_capacity = min(total_units, bucket_capacity)
    if bucket_capacity == 0:
        return 0
    counter = 0
    while total_units != 0:
        for row in grid:
            for i in range(len(row)):
                if row[i] > 0:
                    row[i] -= bucket_capacity
                    if row[i] <= 0:
                        total_units -= (abs(row[i]) + bucket_capacity)
                        row[i] = 0
                        break
        counter += 1
    return counter
