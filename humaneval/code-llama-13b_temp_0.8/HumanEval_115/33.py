
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
    # rows = len(grid)
    # cols = len(grid[0])

    # r_max = math.ceil(rows/bucket_capacity)
    # c_max = math.ceil(cols/bucket_capacity)
    # count = 0

    # # Find how many rows will be filled
    # for row in range(r_max):
    #     # Find how many cols will be filled
    #     for col in range(c_max):
    #         if col == cols or row*bucket_capacity + col >= cols:
    #             break
    #         # For each col, start at bottom and move up
    #         for k in range(bucket_capacity):
    #             if row*bucket_capacity + col + k >= cols:
    #                 break
    #             if grid[row*bucket_capacity + col + k][col] == 1:
    #                 count += 1
    #                 break
    # return count

    # print(r_max)
    # print(c_max)

    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for row in range(rows):
        # find max cols
        for col in range(cols):
            # if grid[row][col] == 1:
            #     count += 1
            #     break
            bucket_capacity = 0
            # print(row, col)
            if col+bucket_capacity <= cols:
                while grid[row][col+bucket_capacity] == 1:
                    # print(row, col)
                    bucket_capacity += 1
                    # print(row, col+bucket_capacity)
                    count += 1
                bucket_capacity = 0
                break
    return count

