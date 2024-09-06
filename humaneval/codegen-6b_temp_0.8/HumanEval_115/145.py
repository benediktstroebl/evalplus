
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
    grid = list(map(list, grid))
    rows, cols = len(grid), len(grid[0])
    fills = [[0]*(cols+1) for _ in range(rows+1)]
    for i in range(rows):
        for j in range(cols):
            fills[i+1][j+1] = fills[i+1][j] + grid[i][j]
    
    def count_fills(cap):
        ret = 0
        for i in range(1, rows+1):
            j = i-1
            while j >= 0 and j >= 1 and fills[j][cap] >= fills[i][cap]:
                j -= 1
            ret = max(ret, j+1)
        for j in range(1, cols+1):
            i = j-1
            while i >= 0 and i >= 1 and fills[cap][i] >= fills[cap][j]:
                i -= 1
            ret = max(ret, i+1)
        return ret
    
    return count_fills(capacity)
