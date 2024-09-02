
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
    def is_well(row, col):
        """
        whether a well at (row, col) is well
        """
        return grid[row][col] == 1

    def is_row_well(row):
        """
        whether all wells at row is well
        """
        return all(is_well(row, col) for col in range(n))

    def is_col_well(col):
        """
        whether all wells at col is well
        """
        return all(is_well(row, col) for row in range(n))

    def get_well_count(row, col):
        """
        get number of wells at row, col
        """
        return sum(is_well(row, col) for col in range(n))

    n = len(grid)
    
    if not n:
        return 0

    cap = capacity
    while cap >= 1:
        w = 0
        for i in range(n):
            if not is_row_well(i):
                # for j in range(n):
                #     if j != i:
                #         if is_well(i, j):
                #             w += 1
                continue
            w += get_well_count(i, 0) - get_well_count(i, n - 1)
        cap -= 1
    return w

