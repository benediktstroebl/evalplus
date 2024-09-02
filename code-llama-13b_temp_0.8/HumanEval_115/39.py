
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
    # # Write your code here

    # # Inputs
    # # grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    # # bucket_capacity = 1

    # # Inputs
    # # grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    # # bucket_capacity = 2

    # # Inputs
    # grid = [[0,0,0], [0,0,0]]
    # bucket_capacity = 5

    # # Outputs
    # # 0

    # # Init
    result = 0
    rows = len(grid)
    cols = len(grid[0])

    # # Main Logic
    for i in range(rows):
        j = 0
        capacity = bucket_capacity
        while j < cols:
            if grid[i][j] == 1:
                if capacity > 0:
                    grid[i][j] = 0
                    capacity -= 1
                else:
                    j += 1
                    capacity = bucket_capacity
            else:
                j += 1
        
        result += math.ceil(sum(grid[i]) / bucket_capacity)

    return result
