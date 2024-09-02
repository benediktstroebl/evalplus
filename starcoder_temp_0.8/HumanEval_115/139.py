
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
    rows = len(grid)
    cols = len(grid[0])
    n_buckets = math.ceil(rows * cols / capacity)
    buckets = [[0 for _ in range(n_buckets)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                buckets[r][c // capacity] += 1

    ans = 0
    for b in buckets:
        total_pos = 0
        for c in b:
            if c!= 0:
                total_pos += 1
        if total_pos == 0:
            continue
        ans += total_pos - max(b)
    return ans
