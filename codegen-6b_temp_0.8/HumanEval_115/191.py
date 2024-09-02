
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
    import math
    grid_len = len(grid[0])
    grid_height = len(grid)
    # print(grid_len, grid_height)
    
    def helper(grid, grid_len, grid_height, capacity, grid_idx, filled):
        if grid_idx >= grid_height:
            return 0
        # print(grid_idx, grid_height)
        current_row = grid[grid_idx]
        buckets_left = capacity
        for i in range(grid_len):
            if current_row[i] == 1:
                # print('current', grid_idx, i, current_row)
                buckets_left -= 1
                if buckets_left < 0:
                    filled += 1
                    if filled >= 2:
                        return 1
                    return helper(grid, grid_len, grid_height, capacity, grid_idx+1, filled)
                # print('value', grid_idx, i, current_row)
                helper(grid, grid_len, grid_height, capacity, grid_idx+1, filled)
        return 0
    
    filled = 0
    capacity = capacity
    return helper(grid, grid_len, grid_height, capacity, 0, filled)

