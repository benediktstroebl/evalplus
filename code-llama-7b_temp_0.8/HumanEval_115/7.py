
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
    import math
    def _max_fill(grid, capacity):
        # Step 1
        # Find the maximum number of buckets we can use
        # We need to find how many 1s we have in the grid and divide it by the
        # capacity of a single bucket
        total_water = 0
        for row in grid:
            total_water += row.count(1)
        return math.ceil(total_water / capacity)

    # Step 2
    # Iterate through the grid
    # When we find a 1, check the amount of water we can extract from it
    # Repeat this process until the grid is empty
    total_extracted_water = 0
    grid_copy = grid.copy()
    while grid_copy:
        # reset max_bucket_count
        max_bucket_count = _max_fill(grid_copy, capacity)
        # update the total extracted water
        total_extracted_water += max_bucket_count
        # iterate through the grid and make the bucket empty
        for row_index, row in enumerate(grid_copy):
            # find the 1
            one_index = row.index(1)
            # update the row
            row[one_index] = 0
            # update the grid
            grid_copy[row_index] = row

    return total_extracted_water


