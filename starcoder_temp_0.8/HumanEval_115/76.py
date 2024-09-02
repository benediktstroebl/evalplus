
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
    # DFS
    n = len(grid)
    m = len(grid[0])
    count = 0

    while True:
        # find the most filled well
        max_num = 0
        max_idx = (0, 0)
        for idx, row in enumerate(grid):
            for idy, element in enumerate(row):
                if element == 0:
                    if max_num < capacity:
                        max_num = capacity
                        max_idx = (idx, idy)
                    break
        
        # fill the well
        for idx, row in enumerate(grid):
            for idy, element in enumerate(row):
                if element == 0:
                    grid[idx][idy] = 1
                    if idx == max_idx[0] and idy == max_idx[1]:
                        continue
                    else:
                        count += 1

        # if we cannot fill any well, then we are done
        if max_num < capacity:
            break

        # fill the well with the capacity
        for idx, row in enumerate(grid):
            for idy, element in enumerate(row):
                if element == 0:
                    if idx == max_idx[0] and idy == max_idx[1]:
                        continue
                    else:
                        grid[idx][idy] = 1
                        count += 1

    return count
