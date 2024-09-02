
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
    n_rows, n_cols = grid.shape
    new_grid = grid.copy()
    # input validation
    if n_rows < 1 or n_cols < 1:
        raise ValueError('grid must be at least 1x1')
    if capacity < 1:
        raise ValueError('capacity must be at least 1')
    # n_rows, n_cols = grid.shape
    grid = grid.flatten()
    grid = grid[grid == 1]
    n_cells = len(grid)
    # number of buckets needed is the ceiling function of the number of cells divided by the capacity
    num_buckets = math.ceil(n_cells / capacity)
    # create n_buckets x n_cols grid
    buckets = np.zeros((num_buckets, n_cols))
    # fill buckets
    for i in range(num_buckets):
        # fill capacity of buckets
        for j in range(capacity):
            # loop over rows (i.e. buckets)
            for k in range(i, num_buckets):
                # loop over cols (i.e. grid)
                for l in range(n_cols):
                    # fill cols as long as there are cells left
                    if grid[0] == 1:
                        buckets[k,l] = 1
                        grid[0] -= 1
                    # if there are no more cells to fill, move to the next bucket
                    else:
                        break
    # fill grid
    for i in range(num_buckets):
        for j in range(n_cols):
            for k in range(i, num_buckets):
                if buckets[k,j] == 1:
                    new_grid[:,j] += 1
    return new_grid
