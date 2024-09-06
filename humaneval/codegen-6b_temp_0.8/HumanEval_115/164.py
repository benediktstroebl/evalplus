
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
    rows, cols = len(grid), len(grid[0])
    sums = [[0]*(cols+1) for _ in range(rows+1)]

    for row in range(1, rows+1):
        for col in range(1, cols+1):
            sums[row][col] = sums[row-1][col] + sums[row][col-1] - sums[row-1][col-1] + grid[row-1][col-1]
    
    res = 0
    for row in range(1, rows+1):
        for col in range(1, cols+1):
            left = col
            for right in range(col, cols+1):
                if left > capacity:
                    break
                res = max(res, right - left)
                left += sums[row][right] - sums[row][col]
                capacity -= 1
    return res

assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6
assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5
assert max_fill([[0,0,0], [0,0,0]], 5) == 0
assert max_fill([[0,0,0]], 1) == 0

