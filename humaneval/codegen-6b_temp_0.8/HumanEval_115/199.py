
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
    # Time: O(columns)
    # Space: O(rows)

    def get_area(grid, row, col):
        area = 0
        for r, c in zip(row, col):
            area += grid[r][c]
        return area

    def get_height_map(grid, rows, cols):
        # Height map is 2D array
        height_map = [[0 for _ in range(cols)] for _ in range(rows)]
        for r, row in enumerate(height_map):
            for c, col in enumerate(row):
                height = 0
                for r2, c2 in zip(rows[r], cols[c]):
                    height = max(height, grid[r2][c2])
                height_map[r][c] = height
        return height_map

    # Get dimension
    rows, cols = len(grid), len(grid[0])
    # Get well dimensions
    well_rows = [sum(row) for row in grid]
    well_cols = [sum(col) for col in map(list, zip(*grid))]
    # Get height map
    well_height_map = get_height_map(grid, well_rows, well_cols)
    # Get number of 'full' wells
    n_full_wells = get_area(grid, well_rows, well_cols)
    # Get capacity of buckets
    bucket_capacity = capacity
    # We don't know the number of times we need to reduce the height of buckets,
    # but we know that we need to reduce all 'full' wells to 'bucket_capacity'
    n_reduce_bucket = math.ceil(n_full_wells / bucket_capacity)
    return n_reduce_bucket

