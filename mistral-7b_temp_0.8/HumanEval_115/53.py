
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
    
    # 0 is free, 1 is water, 2 is water we've extracted
    m, n = len(grid), len(grid[0])

    # Create empty grid to store extracted water
    extracted_grid = [[0 for _ in range(n)] for _ in range(m)]

    # Create lists to store the x and y coordinates of the wells with water
    x_coords, y_coords = [], []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                x_coords.append(i)
                y_coords.append(j)

    # Keep track of the number of water we've extracted
    water_extracted = 0

    # Loop until we've extracted all the water from the wells
    while True:
        # Create a list to store the next row of water we're going to extract
        next_row = []

        # For each well, find the first empty spot in the row to the right
        # If there
