
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
    def complete(grid):
        return sum(sum(row) for row in grid) == 0

    row_count = len(grid)
    col_count = len(grid[0])
    buckets = [[0] * col_count for dummy in range(row_count)]
    capacity = row_count * col_count - sum(sum(row) for row in grid)
    drop_count = 0
    while capacity > 0:
        # print([[b[j] for b in buckets] for j in range(col_count)])
        # print()
        # print(max(buckets, key=lambda x: sum(x)))
        drop_count += 1
        max_row, max_col = max(buckets, key=lambda x: sum(x))
        # print(max_row, max_col)
        if capacity > drop_count * max_row:
            capacity -= drop_count * max_row
            # print(capacity)
            # print(drop_count, max_row, max_col)
        else:
            max_row -= capacity // drop_count
            # print(capacity, drop_count, max_row, max_col)
            capacity = 0
        buckets[max_row][max_col] += capacity // drop_count
        capacity %= drop_count
        # print(capacity)

    return drop_count - 1 if complete(buckets) else -1

