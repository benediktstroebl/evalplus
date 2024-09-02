
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
    
    cols = len(grid[0])
    rows = len(grid)
    res = 0

    def fill_wells(row_idx, col_idx, remaining, visited):
        if not grid[row_idx][col_idx]:
            return remaining
        if remaining == 0:
            return 0
        if row_idx >= rows or col_idx >= cols:
            return remaining
        if (row_idx, col_idx) in visited:
            return remaining
        if row_idx < 0:
            return remaining
        if grid[row_idx][col_idx] == 0:
            return remaining

        if remaining == 1:
            grid[row_idx][col_idx] = 0
            return 0

        visited.add((row_idx, col_idx))
        remaining = fill_wells(row_idx-1, col_idx, remaining-1, visited)
        remaining = fill_wells(row_idx+1, col_idx, remaining-1, visited)
        remaining = fill_wells(row_idx, col_idx-1, remaining-1, visited)
        remaining = fill_wells(row_idx, col_idx+1, remaining-1, visited)
        return remaining

    for col in range(cols):
        for row in range(rows):
            if grid[row][col] == 1:
                visited = set()
                remaining = capacity
                remaining = fill_wells(row, col, remaining, visited)
                res += remaining
    return res

