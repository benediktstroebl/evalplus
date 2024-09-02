
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
    _, siz = len(grid), len(grid[0])
    fill = [[0] * siz for _ in range(siz)]
    row, col = 0, 0
    for i in range(siz):
        for j in range(siz):
            if grid[row][j] == 0:
                fill[row][j] = 1
            elif fill[row][j] < capacity:
                fill[row][j] += 1
            else:
                col = j
                break
        if col == j:
            row += 1
    return row * (row + 1) // 2 - (fill[row][col] if col!= col else 0)

