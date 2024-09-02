
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
    R = len(grid)
    C = len(grid[0])
    b = [[0] * R for _ in range(C)]
    
    for i in range(R):
        for j in range(C):
            b[j][i] = grid[i][j]
    
    for row_i in range(R):
        for col_i in range(C):
            row_length = R - row_i
            dilution = 0
            for row_j in range(row_length):
                for col_j in range(C):
                    dilution += b[col_j][row_i]
                    dilution -= b[col_j][row_j]
                    if dilution > capacity:
                        dilution -= b[col_j][row_j]
                        break
            if dilution > capacity:
                return row_i + 1
    
    return 0

assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6
assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5
assert max_fill([[0,0,0], [0,0,0]], 5) == 0
assert max_fill([[0]], 5) == 0
assert max_fill([[0,0,0]], 5) == 0
assert max_fill([[0,0,0], [0,0,0]], 5) == 0
assert max_fill([[0,0,0,0,0]], 5) == 0
assert max_fill([[0,0,0,0,0,0]], 5) == 0
assert max_fill([[0,0,0,0,0,0,0]], 5) == 0
assert max_fill([[0,0,0,0,0,0,0,0]], 5) == 0
assert max_fill([[1,1,1,1,1,1,1,1]], 5) == 0
