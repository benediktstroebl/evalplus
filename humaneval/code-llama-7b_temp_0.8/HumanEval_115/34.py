
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
    # Time Complexity: O(N), where N is the number of wells
    # Space Complexity: O(N)
    # init variables
    # % operator is modulo
    def max_fill(grid, capacity):
        import math
        # get the number of rows and cols
        n_rows = len(grid)
        n_cols = len(grid[0])
        # get the number of wells
        n_wells = n_rows * n_cols
        # get the number of buckets
        n_buckets = math.floor(n_wells / capacity)
        # return the result
        return n_buckets

    # init variables
    n_rows = len(grid)
    n_cols = len(grid[0])
    # init bucket
    bucket = 0
    # get the number of wells
    n_wells = n_rows * n_cols
    # return the result
    return n_wells

