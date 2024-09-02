
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
    from collections import defaultdict
    # let R be the number of rows, C the number of cols
    nR = len(grid)
    nC = len(grid[0])
    # let W the number of wells
    well_nums = [n for w in range(nR) for i in range(nC) if grid[w][i] == 1]
    # let d be the number of buckets
    d = 0
    for well_num in well_nums:
        d += math.floor(well_num / capacity)

    return d

grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
grid = [[0,0,0], [0,0,0]]