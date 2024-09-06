
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
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Replace any 0 with -1
    grid = [[-1 if val == 0 else val for val in row] for row in grid]

    def get_fills(row, col, fills, capacity, prev_val):
        if (row < 0 or
            row >= num_rows or
            col < 0 or
            col >= num_cols or
            grid[row][col] == -1 or
            grid[row][col] == 0 or
            grid[row][col] == prev_val):
            return fills

        new_grid = [row[:] for row in grid]
        new_grid[row][col] = prev_val

        fills += 1
        fills += get_fills(row + 1, col, fills, capacity, new_grid[row][col])
        fills += get_fills(row - 1, col, fills, capacity, new_grid[row][col])
        fills += get_fills(row, col + 1, fills, capacity, new_grid[row][col])
        fills += get_fills(row, col - 1, fills, capacity, new_grid[row][col])

        return fills

    max_fills = 0
    for row in range(num_rows):
        for col in range(num_cols):
            max_fills = max(max_fills, get_fills(row, col, 0, capacity, grid[row][col]))

    return max_fills
