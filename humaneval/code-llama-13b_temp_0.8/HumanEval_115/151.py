
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
    # # Find the height of the largest rectangle in the histogram
    # # For each well, fill it up to capacity
    # # Keep track of how many fill operations were required
    # # O(n^2) time | O(1) space
    # # n = len(grid)
    # # m = len(grid[0])
    # fill_count = 0
    # for col in range(m):
    #     for row in range(n):
    #         height = grid[row][col]
    #         if height == 0:
    #             continue
    #         height = min(height, capacity)
    #         grid[row][col] = height
    #         fill_count += 1
    #         for row_index in range(row+1, n):
    #             if grid[row_index][col] <= height:
    #                 grid[row_index][col] = height
    #             else:
    #                 break
    # return fill_count
    
    # Find the height of the largest rectangle in the histogram
    # For each well, fill it up to capacity
    # Keep track of how many fill operations were required
    # O(n^2) time | O(1) space
    # n = len(grid)
    # m = len(grid[0])
    fill_count = 0
    for col in range(m):
        height = max_histogram_rectangle(grid[:][col])
        height = min(height, capacity)
        for row in range(n):
            grid[row][col] = height
            fill_count += 1
    return fill_count
