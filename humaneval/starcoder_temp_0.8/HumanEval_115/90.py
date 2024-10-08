
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

    total_cols = len(grid[0])
    total_rows = len(grid)
    total_buckets = math.ceil(total_rows / capacity)
    remaining_rows = total_rows
    remaining_buckets = total_buckets
    current_buckets = 0
    total_filled = 0

    for col_index in range(total_cols):
        for row_index in range(total_rows):
            if grid[row_index][col_index] == 1:
                remaining_rows -= 1
                if remaining_rows == 0:
                    break
                else:
                    if current_buckets == 0:
                        current_buckets = total_buckets
                        remaining_buckets -= 1
                    elif current_buckets > 0:
                        current_buckets -= 1

        total_filled += remaining_buckets
        remaining_rows = total_rows
        if current_buckets!= 0:
            current_buckets = 0
    return total_filled
