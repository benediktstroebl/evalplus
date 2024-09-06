
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

    def water_filled_in_row(row, capacity):
        if len(row) == 0:
            return 0

        water_filled = 0
        current_capacity = capacity
        index = 0

        while index < len(row):
            current_water = row[index]
            if current_capacity >= current_water:
                current_capacity -= current_water
            else:
                water_filled += current_capacity
                current_capacity = capacity - current_water
            index += 1
        return water_filled

    number_of_buckets_filled = 0
    row_index = 0

    while row_index < len(grid):
        row = grid[row_index]
        number_of_buckets_filled += water_filled_in_row(row, capacity)
        row_index += 1
    return number_of_buckets_filled
