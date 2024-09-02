
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
    def lower_buckets(row_index, bucket_capacity):
        nonlocal buckets
        nonlocal water_in_each_row
        nonlocal water_in_each_column

        current_row = row_index

        if(current_row == len(grid)-1):
            return

        for column_index in range(len(grid[current_row])):
            current_column = column_index

            if(current_column == len(grid[current_row])-1):
                return

            current_water = grid[current_row][current_column]
            water_in_each_row[current_row] = water_in_each_row[current_row] + current_water
            water_in_each_column[current_column] = water_in_each_column[current_column] + current_water
            if(water_in_each_row[current_row] > bucket_capacity):
                lower_buckets(current_row+1, bucket_capacity)


    total_rows = len(grid)
    total_columns = len(grid[0])
    buckets = bucket_capacity

    water_in_each_row = [0]*total_rows
    water_in_each_column = [0]*total_columns

    for i in range(total_rows):
        lower_buckets(i, buckets)

    total_water_extracted = sum(water_in_each_column)
    return math.floor(total_water_extracted/buckets)

