
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
    num_row = len(grid)
    num_col = len(grid[0])
    result = 0
    # row_h = [math.ceil(capacity/num_row) for _ in range(num_row)]
    # col_h = [math.ceil(capacity/num_col) for _ in range(num_col)]
    # for i in range(1, num_col):
    #     for j in range(num_row):
    #         grid[j][i] = max(grid[j][i], grid[j][i-1])
    # for i in range(1, num_row):
    #     for j in range(num_col):
    #         grid[i][j] = max(grid[i][j], grid[i-1][j])
    # result = sum(reduce(lambda x, y: x+y, grid[i]) for i in range(num_row))
    for i in grid:
        for j in i:
            if j >= capacity:
                result += 1
            # print(j)
    
    return result

        

    
    
grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
bucket_capacity = 1