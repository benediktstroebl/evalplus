
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
    def _get_well_row(grid, capacity, well_idx, curr_row_idx):
        """
        Return the number of times you need to lower the buckets to empty the well.
        """
        curr_well_row = grid[well_idx]
        num_of_buckets_needed = (1 + curr_well_row.count(1)) // capacity
        return num_of_buckets_needed - 1 if num_of_buckets_needed > 1 else 0

    def _get_total_rows(grid):
        return len(grid)

    total_rows = _get_total_rows(grid)
    total_wells = len(grid[0])
    # Count the number of times we need to lower the buckets to empty the wells.
    num_of_buckets_needed = 0
    for well_idx in range(total_wells):
        num_of_buckets_needed += _get_well_row(grid, capacity, well_idx, 0)
    return num_of_buckets_needed
