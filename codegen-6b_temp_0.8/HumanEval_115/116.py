
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
    n = len(grid)
    m = len(grid[0])

    water_cap = [[0 for i in range(m)] for _ in range(n)]
    for row in range(n):
        for col in range(m):
            water_cap[row][col] = grid[row][col] * capacity

    def get_water_cells(row, col):
        # left, right, top, bottom
        water_cells = set()
        if row + 1 < n:
            water_cells.add(row + 1, col)
        if row - 1 > 0:
            water_cells.add(row - 1, col)
        if col + 1 < m:
            water_cells.add(row, col + 1)
        if col - 1 > 0:
            water_cells.add(row, col - 1)
        return water_cells

    def get_next_cell(row, col):
        # left, right, top, bottom
        next_cells = set()
        if row + 1 < n and water_cap[row + 1][col] > 0:
            next_cells.add((row + 1, col))
        if row - 1 > 0 and water_cap[row - 1][col] > 0:
            next_cells.add((row - 1, col))
        if col + 1 < m and water_cap[row][col + 1] > 0:
            next_cells.add((row, col + 1))
        if col - 1 > 0 and water_cap[row][col - 1] > 0:
            next_cells.add((row, col - 1))
        return next_cells

    def get_closest_well(row, col):
        if row + 1 < n and water_cap[row + 1][col] > 0:
            return row + 1, col
        if row - 1 > 0 and water_cap[row - 1][col] > 0:
            return row - 1, col
        if col + 1 < m and water_cap[row][col + 1] > 0:
            return row, col + 1
        if col - 1 > 0 and water_cap[row][col - 1] > 0