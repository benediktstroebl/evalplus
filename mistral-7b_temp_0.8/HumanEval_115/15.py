
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

    row_count = len(grid)
    column_count = len(grid[0])

    # get minimum number of buckets needed to empty all wells
    min_buckets = math.ceil(row_count * column_count / capacity)

    # determine number of operations needed to empty all wells
    operations = min_buckets

    for i in range(row_count):
        for j in range(column_count):

            # get number of units of water in current well
            water_count = grid[i][j]

            # if water_count <= capacity, fill bucket and empty well
            if water_count <= capacity:
                operations -= 1
                grid[i][j] = 0

            # if water_count > capacity, fill bucket and empty remaining water
            else:
                remaining_water = water_count - capacity
                grid[i][j] -= capacity
                operations -= 1

                # keep track of number of remaining wells
                number_of_wells = 0

                #
