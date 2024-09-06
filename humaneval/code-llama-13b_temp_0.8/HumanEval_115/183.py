
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
    def get_bucket_water(grid, x, y, bucket_capacity):
        # x: well's left
        # y: well's bottom
        # first row
        if x + bucket_capacity >= len(grid[0]):
            return sum(grid[y][x:])
        # last row
        if y + bucket_capacity >= len(grid):
            return sum(grid[y][x:x+bucket_capacity])

        # normal well
        return sum(grid[y][x:x+bucket_capacity])

    # Grid Setup
    # =====================================
    # TODO
    # =====================================

    bucket_capacity = min(bucket_capacity, len(grid))
    min_bucket_capacity = bucket_capacity
    max_bucket_capacity = max(bucket_capacity, math.ceil(len(grid[0]) / len(grid)))
    # print(f'{min_bucket_capacity=} {max_bucket_capacity=}')

    for i in range(min_bucket_capacity, max_bucket_capacity+1):
        # print(f'i={i}')
        # print(grid)
        for row in range(len(grid)-i+1):
            for col in range(len(grid[0])-i+1):
                # print(f'row={row}, col={col}')
                bucket_water = get_bucket_water(grid, col, row, i)
                # print(f'{col}, {row} -> {bucket_water}')
                if bucket_water >= i:
                    grid[row][col] = 0
                    # print(f'row={row}, col={col} -> {bucket_water}')
                    # print(grid)
                    return i

    return -1
