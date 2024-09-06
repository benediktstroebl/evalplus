
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
    # left to right
    # right to left
    # top to bottom
    # bottom to top
    def rtl(grid, cap, visited):
        if len(grid) == 1:
            return 0 if grid[0].count(1) == 0 else len(grid[0]) // cap
        # find all wells
        rows = list()
        cols = list()
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    cols.append(j)
                    rows.append(i)
        if len(cols) == 0:
            return 0
        rows_to_cols = dict()
        for i in range(len(cols)):
            if rows[i] not in rows_to_cols:
                rows_to_cols[rows[i]] = list()
            rows_to_cols[rows[i]].append(cols[i])
        rows_to_cols = {
            k: v for k, v in sorted(rows_to_cols.items(), key=lambda item: -item[0])
        }
        count = 0
        for row in rows_to_cols:
            cols = rows_to_cols[row]
            # sort by val
            cols = sorted(cols)
            # split by capacity
            for i in range(0, len(cols), cap):
                sub_cap = min(cap, len(cols) - i)
                count += 1
        return count
    
    # bottom to top
    def btt(grid, cap, visited):
        if len(grid[0]) == 1:
            return 0 if grid[:,0].count(1) == 0 else len(grid) // cap
        # find all wells
        rows = list()
        cols = list()
        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if col == 1:
                    cols.append(j)
                    rows.append(i)
        if len(cols) == 0:
            return 0
        cols_to_rows = dict()
        for
