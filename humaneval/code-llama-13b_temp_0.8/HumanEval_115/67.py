
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
    # 1. Find the first cell which is full and first cell which is empty
    # 2. Get the maximum of full and empty cells
    # 3. Get the minimum of full and empty cells
    # 4. Move the pointer to empty cell and start filling from empty cell
    # 5. Repeat until minimum > 0
    total_count = 0
    empty_count = 0
    full_count = 0
    total_count = 0
    # 1. Find the first cell which is full and first cell which is empty
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                full_count = i
                break
        else:
            continue
        break
    empty_count = i
    # 2. Get the maximum of full and empty cells
    max_cell_count = max(full_count, len(grid) - 1 - empty_count)
    # 3. Get the minimum of full and empty cells
    min_cell_count = min(full_count, len(grid) - 1 - empty_count)
    # 4. Move the pointer to empty cell and start filling from empty cell
    if full_count < len(grid) - 1 - empty_count:
        # full_count < empty_count
        for i in range(full_count, len(grid) - 1 - empty_count):
            for j in range(len(grid[i])):
                grid[i][j] = 1
            total_count += 1
        # move to next row
        empty_count = len(grid) - 1 - empty_count
        for i in range(full_count, empty_count):
            for j in range(len(grid[i])):
                grid[i][j] = 1
            total_count += 1
    else:
        # full_count > empty_count
        for i in range(empty_count, full_count):
            for j in range(len(grid[i])):
                grid[i][j] = 1
            total_count += 1
       
