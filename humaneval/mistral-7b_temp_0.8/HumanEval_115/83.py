
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
    row_num = len(grid)
    col_num = len(grid[0])
    bucket = capacity
    counts = []
    flag = True
    while flag:
        flag = False
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] > 0:
                    counts.append((i,j))
                    break
            if len(counts) == 0:
                break
            c_i = counts[0][0]
            c_j = counts[0][1]
            if grid[c_i][c_j] < bucket:
                flag = True
                grid[c_i][c_j] -= bucket
                counts.remove((c_i,c_j))
            else:
                bucket -= grid[c_i][c_j]
                grid[c_i][c_j] = 0
                counts.remove((c_i,c_j))
        if len(counts) > 0:
            bucket = capacity
