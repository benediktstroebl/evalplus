
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
    m = len(grid)
    n = len(grid[0])
    capacity = 1
    total_capacity = m * capacity
    buckets = [capacity] * n
    empty_grid = [row[:] for row in grid]
    times = 0

    # special case for when grid is empty
    if not grid:
        return 0

    while empty_grid:
        # find empty wells
        wells = []
        for i in range(m):
            for j in range(n):
                if empty_grid[i][j] == 1:
                    wells.append((i,j))

        # fill all wells
        for well in wells:
            i, j = well
            if empty_grid[i][j] == 1:
                empty_grid[i][j] = 0

                # try to fill all wells in the same row
                for j_ in range(n):
                    if j_ != j and empty_grid[i][j_] == 1:
                        # fill the well
                        empty_grid[i][j_] = 0

                # try to fill all wells in the same column
                for i_ in range(m):
                    if i_ != i and empty_grid[i_][j] == 1:
                        # fill the well
                        empty_grid[i_][j] = 0

        # count number of times to empty the wells
        times += 1

    return times
