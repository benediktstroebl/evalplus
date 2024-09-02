
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

    m = len(grid)
    n = len(grid[0])

    @lru_cache(maxsize=None)
    def get_height(i, j):
        return math.floor(math.log(grid[i][j])+1)

    @lru_cache(maxsize=None)
    def get_bucket_capacity(i, j):
        return math.ceil(capacity/math.pow(2, get_height(i, j)))

    @lru_cache(maxsize=None)
    def get_capacity(i, j):
        if grid[i][j] == 0:
            return 0
        return get_bucket_capacity(i, j)

    @lru_cache(maxsize=None)
    def get_left_capacity(i, j):
        return get_capacity(i, j-1) if j > 0 else 0

    @lru_cache(maxsize=None)
    def get_right_capacity(i, j):
        return get_capacity(i, j+1) if j < n-
