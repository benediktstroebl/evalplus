
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

    # First check if the problem is trivial
    if grid == [[0] * len(grid[0])] * len(grid):
        return 0

    # Initialise the values we'll be using for the TSP 
    # If you don't know what a TSP is, check out the solution.
    cost = 0
    visited = []
    max_wells = 0
    visited_wells = 0
    well_grid = []
    for i in range(len(grid)):
        well_grid.append([i for i in grid[i]])

    # Now, we need to calculate how many wells the bucket can fill up, and use this to calculate the number of
    # times the bucket needs to be lowered
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                well_grid[i][j] = 0

    # Now we need to calculate the total number of wells filled
    for i in range(len(well_grid)):
