
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
    if not grid or not grid[0]:
        return 0
    # the maximum number of wells that need to be filled is equal to the sum of all the ones in the grid
    n_wells = sum(map(sum, grid))
    if capacity <= n_wells:
        return 0

    n_buckets = math.ceil(n_wells / capacity)
    grid = [[-i if j else i for j in row] for i, row in enumerate(grid, start=1)]
    # print(n_buckets, grid)
    for i in range(1, n_buckets):
        grid = [[max(grid[j][i], grid[j][i-1]) for j in range(len(grid))] for i in range(1, len(grid[0]))]
    # print(grid)
    return grid[-1][-1]
