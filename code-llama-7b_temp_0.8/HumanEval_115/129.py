
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
    # Approach:
    # In every well, we have to extract the amount of water equal to the water in that well.
    # So, we first need to find the maximum amount of water each well can contain.
    # To do that, we need to find the maximum number of units of water that can be extracted from a well.
    # To find the maximum water, we first check if the last row has any water.
    # If it does, then we can add the maximum water to the total water.
    # Then, we check the first column. If it has any water, we can add the maximum water to the total water.
    # Now, we check for the minimum of the maximum water in the first column or the maximum water in the last row.
    # This is the maximum water that can be stored in a well.
    # Once we have the maximum water, we need to find the number of times we need to lower the buckets.
    # This is the number of units of water that we need to extract from the well.
    # This is equal to the number of wells in the grid * the maximum water.
    # Then, we check if the total water is greater than the capacity.
    # If it is, then we need to find the minimum of the capacity and the total water.
    # This is the number of units of water that we need to extract from each well.
    # Then, we need to subtract this amount of water from the total water.
    # Finally, we return the number of times we need to lower the buckets.
    # This is the minimum of the number of times we need to lower the buckets and the number of wells.

    # Find the maximum number of units of water in a well.
    def max_water(grid, capacity):
        # Find the maximum water in the last row.
        last_row = grid[-1]
        water = 0
        for x in last_row:
            if x == 1:
                water += 1
        
        # Find the maximum water in the first column.
        first_column = [x[0] for x in grid]
        for x in first_column:
            if x == 1:
                water += 1

        # Find the minimum of the
