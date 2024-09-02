
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
    if not grid or not capacity:
        return 0

    m = len(grid)
    n = len(grid[0])
    rows = []
    columns = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                columns.append(j)
                rows.append(i)
    columns = list(set(columns))
    columns.sort()
    rows = list(set(rows))
    rows.sort()

    def col_fill(start_col, end_col, depth):
        for i in range(start_col, end_col):
            col_max = depth
            for row_index in range(m):
                if grid[row_index][i] == 1:
                    col_max = max(col_max, row_index)
            for row_index in range(col_max, -1, -1):
                if grid[row_index][i] == 1:
                    grid[row_index][i] = 0

    def row_fill(start_row, end_row, depth):
        for i in range(start_row, end_row):
            row_max = depth
            for col_index in range(n):
                if grid[i][col_index] == 1:
                    row_max = max(row_max, col_index)
            for col_index in range(row_max, -1, -1):
                if grid[i][col_index] == 1:
                    grid[i][col_index] = 0

    def fill(start, end, is_row):
        fill_count = 0
        for i in range(start, end):
            if is_row:
                row_max = None
                for j in range(n):
                    if grid[i][j] == 1:
                        row_max = max(row_max, j)
                fill_count += math.ceil((row_max + 1) / capacity)
            else:
                col_max = None
                for j in range(m):
                    if
