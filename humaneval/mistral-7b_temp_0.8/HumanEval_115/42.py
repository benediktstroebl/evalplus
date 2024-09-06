
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

    # if no wells need filling, return 0
    if not grid or not grid[0]:
        return 0

    # initialize the number of times to empty a well
    fillings = 0

    # keep iterating through all the wells
    for i in range(len(grid)):

        # if this row is empty, keep iterating
        if not grid[i]:
            continue

        # initialize the number of times this well has been filled
        fillings_needed = 0

        # check each cell in this row for water
        for j in range(len(grid[i])):

            # if there is water, add to the number of times needed to fill this well
            if grid[i][j] == 1:
                fillings_needed += 1

        # if this well needs to be filled, add the number of times needed to fill it to the number of times needed to fill all the wells
        if fillings_needed:
            fillings += fillings_needed

    # if the number of times needed to fill all the
