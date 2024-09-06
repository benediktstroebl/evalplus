
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
    rows = len(grid)
    cols = len(grid[0])
    row_count = [0] * rows
    col_count = [0] * cols
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            if grid[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1
            j += 1
        i += 1
    # print(row_count)
    # print(col_count)
    count = 0
    while capacity > 0:
        # print(capacity)
        i = 0
        while i < rows:
            if row_count[i] == capacity:
                row_count[i] = 0
                j = 0
                while j < cols:
                    if grid[i][j] == 1:
                        row_count[i] += 1
                        col_count[j] -= 1
                    j += 1
                capacity -= 1
                count += 1
                i = -1
            i += 1
        # print(row_count)
        # print(col_count)
        j = 0
        while j < cols:
            if col_count[j] == capacity:
                col_count[j] = 0
                i = 0
                while i < rows:
                    if grid[i][j] == 1:
                        row_count[i] -= 1
                        col_count[j] += 1
                    i += 1
                capacity -= 1
                count += 1
                j = -1
            j += 1
        # print(row_count)
        # print(col_count)
    return count

