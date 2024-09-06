
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
    row_count = len(grid)
    col_count = len(grid[0])

    if not grid or not grid[0]: # Empty grid is impossible
        return 0

    # Check if grid[0] is full
    if grid[0][0] == 1:
        return math.inf

    col_tracker = [0] * col_count
    # Track max_so_far
    max_so_far = 0
    for row in grid:
        for col_idx, cell in enumerate(row):
            if cell == 1:
                col_tracker[col_idx] += 1
            max_so_far = max(max_so_far, col_tracker[col_idx])
    
    # Adjust col_tracker
    # After adjusting, we would get a row with full wells of row_count
    # After this loop, we would have full wells for each col_tracker
    # Execute this loop until full wells satisfy max_so_far condition
    while max_so_far > capacity:
        # Find empty wells of empty rows
        row_need_to_fill = [idx for idx, cell in enumerate(col_tracker) if cell == 0]
        row_need_to_fill.reverse()
        if not row_need_to_fill:
            break
        # Fetch empty wells until full wells satisfy max_so_far condition
        max_so_far_wells = 0
        for row_idx, row_idx_to_fill in enumerate(row_need_to_fill):
            max_so_far_wells = max(max_so_far_wells, bucket_capacity - row_tracker[row_idx])
            for col_idx, cell in enumerate(grid[row_idx]):
                if col_idx <= row_idx_to_fill:
                    continue
                col_tracker[col_idx] += 1

        max_so_far -= max_so_far_wells

    return max_so_far

