
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
    # init grid variables
    grid_rows, grid_cols = len(grid), len(grid[0])
    # init visited
    visited = [[False for _ in range(grid_cols)] for _ in range(grid_rows)]

    # count number of times to fill
    count = 0
    # loop grid rows
    for row in range(grid_rows):
        # loop grid columns
        for col in range(grid_cols):
            # if current cell is 1 and is not visited
            if grid[row][col] == 1 and not visited[row][col]:
                # find number of full buckets needed to empty current cell
                full_buckets = find_full_buckets(grid, row, col, visited, capacity)
                # add current row and column to visited
                visited[row][col] = True
                # add count
                count += full_buckets
    return count

