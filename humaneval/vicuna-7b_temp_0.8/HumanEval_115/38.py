
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

    rows, cols = grid.shape

    # create a dictionary to store the number of times each well is visited
    visited = {}

    # initialize the number of times each well is visited
    for i in range(rows):
        visited[i] = 0

    # initialize the number of times each well is visited
    for j in range(cols):
        visited[0] = 0

    # loop through all the wells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # if the well is not visited, add it to the dictionary
                visited[j] = 1
                # if the well is not empty, add the number of times it is visited
                if grid[i][j] == 1:
                    visited[j] += 1
                # if the well is not empty, add the number of times it is visited
                # if the well is not the current well
                if j != i:
                    visited[j] += 1
                # if the well is not empty, add the number of times it is visited
                # if the well is not the current well, not empty, not visited
                if grid[i][j] == 1 and grid[i][j] != 0 and grid[i][j] != 1:
                    visited[j] += 1

    # loop through all the wells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # if the well is not visited, add it to the dictionary
                visited[j] = 1
                # if the well is not empty, add the number of times it is visited
                if grid[i][j] == 1:
                    visited[j] += 1
                # if the well is not empty, add the number of times it is visited
                # if the well is not the current well
                if j != i:
                    visited[j] += 1
                # if the well is not empty, add the number of times it is visited
                # if the well is not the current well, not empty, not visited
               
