
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
    # Your code here
    
    # Solution:
    # 1. Find the maximum capacity in top row and the left column
    # 2. Find the number of times you can fill one row (range top to bottom)
    # 3. Find the number of times you can fill one column (range left to right)
    # 4. Find the number of times you can fill two rows and one column
    
    # So we can solve this in O(n) and O(n) time complexity, where n is the number of wells
    
    ## Solution 1
    # row_max = [0 for _ in range(len(grid))]
    # for row in grid:
    #     row_max_idx, row_max_val = max(enumerate(row), key=lambda x:x[1])
    #     row_max[row_max_idx] = row_max_val
    
    # col_max = [0 for _ in range(len(grid[0]))]
    # for col in map(list, zip(*grid)):
    #     col_max_idx, col_max_val = max(enumerate(col), key=lambda x:x[1])
    #     col_max[col_max_idx] = col_max_val
    
    # count = 0
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == 1:
    #             if row_max[i] >= bucket_capacity:
    #                 count += row_max[i]//bucket_capacity
    #             if col_max[j] >= bucket_capacity:
    #                 count += col_max[j]//bucket_capacity
    # return count
    
    ## Solution 2
    # row_max = [0 for _ in range(len(grid))]
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == 0:
    #             continue
    #         row_max[i] = max(row_