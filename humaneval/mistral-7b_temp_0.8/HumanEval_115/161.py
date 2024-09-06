
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

    # calculate the number of columns and rows in the grid
    rows = len(grid)
    cols = len(grid[0])

    # initialize a matrix to store the number of times each bucket was used
    buckets_used = [[0] * cols for _ in range(rows)]

    # iterate over all rows and columns in the grid
    for i in range(rows):
        for j in range(cols):
            # if the current cell is 0, we don't need to do anything
            if grid[i][j] == 0:
                continue

            # if the cell is 1, we need to fill the bucket
            grid[i][j] = 0

            # calculate the number of times the bucket needs to be lowered
            times = 1
            while grid[i][j] < capacity:
                # if the bucket is full, we need to lower it
                if grid[i][j] + 1 >= capacity:
                    grid[i][j] += 1
                    buckets_used[i][j] += 1
