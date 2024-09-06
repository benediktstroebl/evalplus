
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

    # Calculate the size of the grid
    size = len(grid)
    # Calculate the number of wells
    n_wells = sum(1 for i in grid for j in i if j)

    # Calculate the maximum number of times we can lower the bucket
    max_bucket_fills = math.ceil(n_wells / capacity)

    # The number of times we need to lower the bucket
    bucket_fills = max_bucket_fills

    # Fetch the indexes of the wells
    wells = []
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 1:
                wells.append([i, j])

    # For each well
    for well in wells:
        # Check if we can fill the bucket with water from the well
        if grid[well[0]][well[1]] > 0:
            # Fill the bucket with water from the well
            grid[well[0]][well[1]] -= 1
            # Reduce the number
