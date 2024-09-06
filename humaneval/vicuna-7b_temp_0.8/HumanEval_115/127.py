
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
    if grid is None or grid == [0, 0, 0, 0]:
        return 0
    else:
        n = len(grid)
        m = grid[0].length
        for i in range(1, n):
            for j in range(1, m):
                if grid[i][j] == 1:
                    # add the bucket to the grid
                    bucket_grid = [[0, 0] for _ in range(m)]
                    bucket_grid[0][j] = 1
                    bucket_grid[1][j] = 1
                    for k in range(2, m):
                        if grid[i][k] == 1:
                            bucket_grid[k][j] = 1
                        else:
                            bucket_grid[k][j] = 0

                    # check if all wells are full
                    full_grid = [[0] * m for _ in range(n)]
                    for i in range(n):
                        for k in range(m):
                            if grid[i][k] == 1:
                                full_grid[i][k] = 1
                            else:
                                full_grid[i][k] = 0

                    if full_grid.count(1):
                        return max(max(full_grid.flatten()), bucket_grid.flatten())

        return max(max(bucket_grid.flatten()), max(max(full_grid.flatten()), bucket_grid.flatten()))
