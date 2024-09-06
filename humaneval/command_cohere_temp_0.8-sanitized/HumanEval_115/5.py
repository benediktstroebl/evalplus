import math
def max_fill(grid, capacity):
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
    # One dimensional pass
    max_fill = 0
    for i in range(len(grid)):
        j = 0
        while grid[i][j] == 1:
            if capacity < j + 1:
                return -1
            capacity -= j + 1
            max_fill += 1
            j += 1
    
    # Two dimensional pass
    i = 0
    while i < len(grid) - 1:
        j = 0
        while j < len(grid[i]) - 1:
            if grid[i][j] == 1 and grid[i + 1][j] == 1:
                if capacity < 2:
                    return -1
                capacity -= 2
                max_fill += 1
                i += 1
                j += 1
            elif grid[i][j] == 1:
                if capacity < 1:
                    return -1
                capacity -= 1
                max_fill += 1
                j += 1
            else:
                j += 1
        i += 1
    
    return max_fill