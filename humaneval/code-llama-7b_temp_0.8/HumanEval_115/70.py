
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

    #    1. Initialize the bucket_capacity and number of columns
    #    2. Traverse the grid and count the number of water units in the grid
    #    3. Find the number of times to lower the bucket
    #    4. Return the number of times to lower the bucket

    # 1. Initialize the bucket_capacity and number of columns
    # grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    # bucket_capacity = 1
    # well_units = 0
    # rows, columns = len(grid), len(grid[0])
    # well_units = 0
    # for row in range(rows):
    #     for column in range(columns):
    #         if grid[row][column] == 1:
    #             well_units += 1
    # print(well_units)

    # 2. Traverse the grid and count the number of water units in the grid
    # well_units = 0
    # for row in range(rows):
    #     for column in range(columns):
    #         if grid[row][column] == 1:
    #             well_units += 1
    # print(well_units)

    # 3. Find the number of times to lower the bucket
    # no_of_times_to_lower_bucket = math.ceil(well_units / bucket_capacity)
    # print(no_of_times_to_lower_bucket)

    # 4. Return the number of times to lower the bucket
    # return no_of_times_to_lower_bucket

    # def max_fill(grid, bucket_capacity):
    #     # Time complexity: O(R*C)
    #     # Space complexity: O(1)
    #     well_units = 0
    #     rows, columns = len(grid), len(grid[0])
    #     for row in range(rows):
    #         for column in range(columns):
    #             if grid[row][column] == 1:
    #                
