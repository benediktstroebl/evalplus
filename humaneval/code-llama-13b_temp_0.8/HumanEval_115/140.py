
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
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # Caching the values of total rows and columns
    rows = len(grid)
    cols = len(grid[0])
    # The total number of times the buckets are filled
    times = 0

    # Initializing a copy of the grid and populating it with 0s
    grid_copy = []
    for row in range(rows):
        grid_copy.append([])
        for col in range(cols):
            grid_copy[row].append(0)
    
    # Iterating over every row
    for row in range(rows):
        # Iterating over every column
        for col in range(cols):
            # Checking if the current value is a 1 (a filled well)
            if grid[row][col] == 1:
                # Iterating over the 2 possible bucket orientations
                for orient in range(2):
                    # Setting the current orientation for the bucket
                    orientation = (row, col)
                    # Initializing the current bucket capacity
                    bucket_capacity = 0
                    # Filling the bucket with water
                    while orientation[orient] >= 0 and orientation[orient] < rows and bucket_capacity <= capacity:
                        # If the current value is a 1 (filled well)
                        if grid[orientation[0]][orientation[1]] == 1:
                            # Increasing the bucket capacity by 1
                            bucket_capacity += 1
                            # Marking the filled well as 0
                            grid_copy[orientation[0]][orientation[1]] = 0
                        if orient == 0:
                            # Decreasing the row index of the bucket
                            orientation = (orientation[0] - 1, orientation[1])
                        else:
                            # Increasing the column index of the bucket
                            orientation = (orientation[0], orientation[1] + 1)
                    # Increasing the number of times the buckets are filled
                    times += 1
    # Returning the total number of times the bu
