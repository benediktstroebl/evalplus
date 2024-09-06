
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
    def is_valid(cell):
        return 0 <= cell[0] < len(grid) and 0 <= cell[1] < len(grid[0])

    def get_bucket(cell):
        return grid[cell[0]][cell[1]]
    
    def get_next_cell(cell):
        if cell[1] == len(grid[0]) - 1:
            return (cell[0] , 0)
        return (cell[0] , cell[1] + 1)

    def get_water(cell):
        return grid[cell[0]][cell[1]]
    
    def is_empty(cell, bucket):
        return cell[1] == len(grid[0]) - 1 and bucket == 0

    def get_capacity(cell, bucket):
        if cell[1] == len(grid[0]) - 1:
            return bucket
        return 0

    def add_water(cell, bucket, capacity):
        if bucket == 0:
            return False
        return grid[cell[0]][cell[1]] > capacity

    def is_full(cell, bucket):
        return cell[1] == len(grid[0]) - 1 and bucket > 0

    def fill_bucket(cell, bucket):
        if is_valid(cell) and get_capacity(cell, bucket) > 0:
            grid[cell[0]][cell[1]] -= bucket
            return True
        return False

    # Variable to store the maximum number of units that can be extracted from any well
    max_water = 0
    # Variable to store the number of times we need to lower the buckets
    num_of_times = 0

    for i in range(len(grid)):
        # Each row
        for j in range(len(grid[0])):
            # Every element in the row
            cell = (i, j)
            # Get the current bucket
            bucket = get_bucket(cell)

            # Add water from the well
            if fill_bucket(cell, bucket):
                num_of_times += 1
                # Get the number of units
                max_water = max(max_water, get_water(cell))

            # Add