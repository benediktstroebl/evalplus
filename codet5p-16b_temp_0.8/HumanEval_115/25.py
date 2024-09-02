
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

    n = len(grid[0])
    m = len(grid)

    def fill_bucket(bucket):
        nonlocal grid
        if not bucket: return 0
        ret = math.inf
        for i in range(m):
            for j in range(n):
                if bucket[i][j] == 1:
                    ret = min(ret, fill_bucket(bucket[:i]+[[0]*n]+bucket[i+1:]))
                    ret = min(ret, fill_bucket(bucket[:i]+[[1]*n]+bucket[i+1:]))
                    ret = min(ret, fill_bucket(bucket[:i]+[[0,0,0,0]]+bucket[i+1:]))
                    ret = min(ret, fill_bucket(bucket[:i]+[[0,0,0,0], [0,0,0,0]]+bucket[i+1:]))
        return ret+1

    return fill_bucket([[1 if grid[i][j] else 0 for j in range
