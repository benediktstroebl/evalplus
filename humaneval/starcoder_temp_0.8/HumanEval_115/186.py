
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
    n_rows = len(grid)
    if n_rows == 0:
        return 0
    n_cols = len(grid[0])
    if n_cols == 0:
        return 0

    def recursive_fill(row, col, fill_count):
        """
        Fill all wells from (row, col)
        """
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols or grid[row][col] == 0:
            return
        elif grid[row][col] == 1:
            grid[row][col] = 0
            fill_count += 1
            if fill_count == capacity:
                return
            recursive_fill(row - 1, col, fill_count)
            recursive_fill(row + 1, col, fill_count)
            recursive_fill(row, col - 1, fill_count)
            recursive_fill(row, col + 1, fill_count)
        return fill_count

    max_fill_count = 0
    for row in range(n_rows):
        for col in range(n_cols):
            if grid[row][col] == 1:
                fill_count = recursive_fill(row, col, 0)
                max_fill_count = max(max_fill_count, fill_count)
    return max_fill_count

