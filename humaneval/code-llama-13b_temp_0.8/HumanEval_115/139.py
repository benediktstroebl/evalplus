
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

    buckets = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                buckets.append([i,j])

    buckets_grid = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    
    for bucket in buckets:
        y, x = bucket
        for i in range(x+1, len(grid[0])):
            if grid[y][i] == 1:
                buckets_grid[y][i] = True
            else:
                break
        for j in range(y+1, len(grid)):
            if grid[j][x] == 1:
                buckets_grid[j][x] = True
            else:
                break
    
    # print("buckets_grid:")
    # for row in buckets_grid:
    #     print(row)
    
    max_fill = 0
    for i in range(len(grid[0])):
        if buckets_grid[0][i]:
            max_fill = math.ceil(max_fill/2)
        else:
            max_fill += 1
    
    for i in range(1, len(grid)):
        if buckets_grid[i][0]:
            max_fill = math.ceil(max_fill/2)
        else:
            max_fill += 1

    return max_fill
