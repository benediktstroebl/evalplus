
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
    # test if grid is empty
    if len(grid) == 0:
        return 0
    # check if the bucket capacity is more than the grid
    if capacity > sum(sum(row) for row in grid):
        return 0
    # check if the grid is empty
    if len(grid[0]) == 0:
        return 0
    # check if all the rows are 0
    if len(set(row) for row in grid) == 1:
        return 0
    # check if all the colums are 0
    if len(set(row) for row in zip(*grid)) == 1:
        return 0
    # sort the grid into a dictionary
    dictionary = {}
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == 1:
                dictionary[i,j] = 0
            else:
                dictionary[i,j] = 1

    # check if all the values are equal to 1
    if len(set(val for i, val in
