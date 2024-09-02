
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
    # write your code here
    grid = grid.tolist()
    bucket_capacity = max(bucket_capacity, grid[0][0])
    for row in grid:
        if row == [0] * len(row):
            return 0
        for col in range(len(row)):
            if row[col] == 1:
                max_height = 0
                max_index = 0
                for i in range(1, len(row)):
                    for j in range(col, len(row)):
                        if row[j] == 1 and (i-1 >= 0 or j-1 >= 0):
                            max_height = max(max_height, col-j+1)
                            max_index = i-1 if max_height == j-1 else j-1
                if max_height > bucket_capacity:
                    return col+1 + max_index
    return 0