
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
    # max_cols = len(grid[0])
    # max_rows = len(grid)
    # bucket_count = max_cols

    # # get all 1's in grid
    # locations = []
    # for r in range(max_rows):
    #     for c in range(max_cols):
    #         if grid[r][c] == 1:
    #             locations.append((r,c))
    
    # # count the number of 1's in each row
    # row_counts = [0] * max_rows
    # for loc in locations:
    #     row_counts[loc[0]] += 1

    # # compute max_row_count
    # max_row_count = max(row_counts)

    # # compute the number of times to lower the buckets
    # return math.ceil(max_row_count / bucket_count)
    # return max_row_count // bucket_count
    # return max_row_count / bucket_count
    # return max_row_count / bucket_count + 1
    # return max_row_count * bucket_count - bucket_count

    # import math

    # count = 0
    # n = len(grid)
    # m = len(grid[0])
    # if not (n and m):
    #     return 0
    # bucket_capacity = 1

    # water_in_bucket = 0
    # row_index = 0

    # while row_index < n:
    #     while (row_index < n) and (water_in_bucket < bucket_capacity):
    #         row = grid[row_index]
    #         cell_index = 0

    #         while cell_index < m and row[cell_index] != 1:
    #             cell_index += 1

    #         if cell_index < m:
    #             water_in_bucket += 1
    #             cell_index += 1
    #         else:
    #             row_index += 1

    #     while (row_index <
