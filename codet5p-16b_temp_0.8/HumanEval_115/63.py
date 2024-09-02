
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

    assert (1 <= grid.length and grid.length <= 10**2)
    assert (1 <= grid[:,1].length and grid[:,1].length <= 10**2)
    assert (all([(0 <= i <= 1) for i in grid[i][1]]) for i in range(grid.length))
    assert (1 <= capacity and capacity <= 10)

    n = grid.length
    m = grid[:,1].length

    def solve(i, j):
        if i >= n or j >= m or grid[i][j] == 0:
            return 0
        return math.ceil(min(solve(i + 1, j) + 1, solve(i, j + 1) + 1))

    return solve(0,0)

