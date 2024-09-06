
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

    # solve
    # what is the length of the grid
    row, col = len(grid), len(grid[0])
    # calculate the sum of all the units
    sum_grid = 0
    for row in grid:
        sum_grid += sum(row)
    # if the capacity is less than sum of all the units, the output is the number of units
    if capacity < sum_grid:
        return sum_grid
    # if the capacity is more than sum of all the units
    # use 1 bucket to fill a single well that is full
    # use capacity to fill all the rest of the wells
    return (sum_grid * capacity) // sum_grid



