
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
    # A: get empty wells
    # B: get number of buckets needed
    # C: return number of times needed
    n_buckets = capacity
    n_wells = len(grid)
    empty_wells = []
    for i in range(n_wells):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                empty_wells.append((i,j))
    # B: get number of buckets needed
    # Try with one bucket to get the maximum
    if len(empty_wells) <= n_buckets:
        return len(empty_wells)
    else:
        n_buckets = math.floor(len(empty_wells)/n_buckets)

    # C: return number of times needed
    return n_buckets
