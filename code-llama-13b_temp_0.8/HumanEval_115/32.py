
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

    # To solve the problem, I will use a matrix to represent the water in each well and the empty space that can be 
    # filled with water
    filled = [[0] * len(grid[0]) for _ in range(len(grid))]
    for i in range(len(filled)):
        for j in range(len(filled[i])):
            if grid[i][j] == 1:
                filled[i][j] = 1
            elif i == len(filled)-1:
                filled[i][j] = 1
            elif filled[i+1][j] == 1:
                filled[i][j] = 1
            else:
                filled[i][j] = 0

    for i in range(len(filled)-2, -1, -1):
        for j in range(len(filled[i])):
            if filled[i+1][j] == 1:
                filled[i][j] = 1
            elif filled[i+1][j-1] == 1:
                filled[i][j] = 1
            elif filled[i+1][j+1] == 1:
                filled[i][j] = 1

    result = 0
    for i in range(len(filled)):
        for j in range(len(filled[i])):
            if filled[i][j] == 0:
                result += 1

    return math.ceil(result / capacity)

