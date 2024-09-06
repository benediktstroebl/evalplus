
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
    if grid.length == 0:
        return 0
    
    #
    # Find the starting well
    #
    start = max(grid, key=lambda x: x[0])

    #
    # Check if all wells are empty
    #
    all_empty = True
    for i in range(start.shape[0]):
        for j in range(start.shape[1]):
            if grid[i][j] == 1:
                all_empty = False
                break
    
    if all_empty:
        return 0
    
    #
    # Fill the wells
    #
    for i in range(start.shape[0]):
        for j in range(start.shape[1]):
            if grid[i][j] == 1:
                bucket_index = start[0][j]
                while grid[i][j] == 1:
                    bucket_index = (bucket_index + 1) % bucket_capacity
                grid[i][j] = bucket_index
    
    #
    # Fill the rest of the wells
    #
    for i in range(start.shape[0]):
        for j in range(start.shape[1]):
            if grid[i][j] == 0:
                bucket_index = start[0][j]
                while grid[i][j] == 0:
                    bucket_index = (bucket_index + 1) % bucket_capacity
                grid[i][j] = bucket_index
    
    #
    # Find the end well
    #
    end = max(grid, key=lambda x: x[0])
    while end[0][0] != 0:
        end = end[1:]
        for i in range(len(end)):
            for j in range(len(end[i])):
                if end[i][j] == 1:
                    bucket_index = end[i][j]
                    while end[i][j] == 1:
                        bucket_index = (bucket_index + 1) % bucket_capacity
                    end[i][j
