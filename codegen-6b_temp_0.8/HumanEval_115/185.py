
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
    # two pointer arrays
    row_heights = []
    col_widths = []

    for r in grid:
        heights = [0]
        for c in r:
            if c:
                heights.append(heights[-1] + 1)
            else:
                heights.append(0)
        row_heights.append(heights)

    for c in zip(*grid):
        col_widths.append([0] + [c.count(1) for c in zip(*grid)])

    b_size = capacity

    def is_lowered(x, y):
        if x == 0 or y == 0:
            return False

        return row_heights[x][y] >= row_heights[x - 1][y] \
            and col_widths[x][y] >= col_widths[x][y - 1]

    def make_buckets(x, y, b):
        if b == 0:
            return

        if is_lowered(x, y) and not is_lowered(x-1, y):
            make_buckets(x-1, y, b - 1)
        elif is_lowered(x, y) and is_lowered(x-1, y-1):
            make_buckets(x - 1, y - 1, b - 1)
        else:
            make_buckets(x, y-1, b)
            make_buckets(x-1, y, b)

    make_buckets(len(grid) - 1, len(grid[0]) - 1, b_size)

    return sum(x.count(1) for x in zip(*grid)) + sum(x.count(1) for x in grid)

