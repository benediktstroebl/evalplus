
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

    # Copy grid to avoid in-place modifications
    grid = list(map(list, grid))
    
    # Determine the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # Determine the number of times we will need to lower the buckets
    # The number of times we need to lower is equal to the number of
    # wells in the grid
    times = 0

    # Determine the number of buckets and their capacity
    num_buckets = rows * cols
    bucket_capacity = capacity

    # Loop through the grid and count the wells
    for row in grid:
        times += row.count(1)

    # If the number of wells is less than the number of buckets
    # then we only need to lower the buckets once
    if times < num_buckets:
        return 1
    
    # If the number of wells is greater than or equal to the number of buckets
    # then we will need to lower the buckets
    # more than once (less than or equal to math.ceil(times / num_buckets)) times
    # For each iteration of the loop, we will determine the number of water
    # we can extract from each row
    # The number of water we can extract from each row depends on the water
    # we have left to extract
    for i in range(1, math.ceil(times / num_buckets) + 1):
        for row in range(rows):
            # Keep track of the starting column for each row
            col = 0

            # Keep track of the number of water we have extracted
            water_extracted = 0

            # While we haven't extracted enough water
            while water_extracted < bucket_capacity:
                # If the cell is a well
                if grid[row][col] == 1:
                    # Extract one unit of water from the well
                    grid[row][col] = 0
                    water_extracted += 1
                    # Move to the next column
                    col += 1
                # If the cell is not a well
                else:
                   
