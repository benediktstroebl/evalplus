
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
    if not grid:
        return 0
    grid_length = len(grid)
    bucket_capacity = max(1, capacity)
    count = 0
    for row in grid:
        if row == [0,]*grid_length:
            # all wells are empty
            for i in range(grid_length):
                for j in range(grid_length):
                    if grid[i][j] == 1:
                        # if one of the wells is full, we can't empty the others
                        return count
                    else:
                        # otherwise, we can empty all the wells in the same row
                        break
            count += 1
            continue
    # all wells have the same length
    for i in range(grid_length):
        for j in range(grid_length):
            if grid[i][j] == 1:
                count += 1
                for bucket_index in range(bucket_capacity):
                    for k in range(grid_length):
                        for l in range(grid_length):
                            if (k,l) != (i,j) and grid[k][l] == 1:
                                # if we have a full well in the same row and same bucket,
                                # we can't empty any of the wells
                                return count
    return count

grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
grid = [[0,0,0,0], [0,0,0,0]]
grid = [[0,0,0]]
