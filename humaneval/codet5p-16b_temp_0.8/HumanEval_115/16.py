
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
    memo = {}
    def fill_well(i, j, capacity):
        if (i, j) in memo: return memo[(i, j)]
        if capacity == 0:
            memo[(i, j)] = 0
            return 0
        if i == 0:
            memo[(i, j)] = math.inf
            return math.inf
        if j == 0:
            memo[(i, j)] = max(fill_well(i-1, j, capacity), fill_well(i, j+1, capacity-1))
        else:
            memo[(i, j)] = min(fill_well(i-1, j, capacity), fill_well(i, j+1, capacity-1)) + 1
        return memo[(i, j)]

    def fill_well_2(i, j, capacity):
        if capacity == 0: return 0
        if i == 0: return math.inf
        if j == 0: return max(fill_well_2(
