
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
    if capacity < 1:
        return 0

    num_columns = len(grid[0])
    if num_columns < 1:
        return 0

    # The bottle can't fill the last column.
    for i in range(len(grid)):
        if grid[i][num_columns - 1] == 1:
            return math.inf

    # Calculate the maximum distance (number of columns) to travel
    # in order to fill the bottle.
    max_distance = 0
    for i in range(len(grid)):
        for j in range(num_columns - 1, -1, -1):
            if grid[i][j] == 1:
                max_distance = num_columns - j - 1
                break

    # Divide the columns in two parts:
    # 1. The first part is the maximum distance (max_distance) to travel in 
    #    order to fill the bottle.
    # 2. The second part is the rest of the columns.
    if max_distance > 0:
        bottle_1 = grid
        for i in range(len(grid)):
            bottle_1[i][num_columns - max_distance - 1] = 0

        bottle_2 = []
        for i in range(len(grid)):
            bottle_2.append(grid[i][num_columns - max_distance:])

        return max_fill(bottle_1, capacity) + max_fill(bottle_2, capacity)
    
    # Calculate the maximum capacity of the bottle.
    max_capacity = 0
    for i in range(len(grid)):
        for j in range(num_columns):
            if grid[i][j] == 1:
                max_capacity = max(max_capacity, capacity - j)

    return max_capacity
