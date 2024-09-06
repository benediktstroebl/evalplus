
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
    grid = [int(grid_row) for grid_row in grid]
    bucket_capacity = int(bucket_capacity)

    # place initial water
    for row in grid:
        row.append(1)

    # move water from leftmost well to rightmost well
    i = 0
    for j in range(len(grid)-1, -1, -1):
        grid[i][j] = grid[i][j-1]
        i += 1

    # remove water from well to fill buckets
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                # check if bucket can be filled
                if j == 0:
                    # no need to fill bucket as it is not full yet
                    continue
                else:
                    if grid[i-1][j] == 1:
                        # no need to fill bucket as it is not full yet
                        continue
                    else:
                        grid[i-1][j] = 1
                        grid[i][j] = 0
                        bucket_count = 1
                        for k in range(j-1, -1, -1):
                            grid[i-1][k] = 0
                        bucket_count += 1
                        grid[i][j] = bucket_count
                        for k in range(j-1, -1, -1):
                            grid[i-1][k] = 1
                        grid[i][j] = 1
                        for k in range(j-1, -1, -1):
                            grid[i-1][k] = 0
        if i == 0:
            break

    return grid[0][0]