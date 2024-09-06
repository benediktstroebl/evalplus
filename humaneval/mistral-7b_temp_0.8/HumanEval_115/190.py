
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

    # O(n) time | O(1) space
    row, col = len(grid), len(grid[0])

    col_count, row_count = 0, 0

    while col_count < col or row_count < row:
        # The next row is empty
        if grid[row_count][col_count] == 0:
            row_count += 1
            continue

        # Iterate along the current row
        for col_iter in range(col_count, col):
            # The bucket is full
            if grid[row_count][col_iter] + grid[row_count][col_count] > capacity:
                col_count = col_iter
                break

            # The bucket is not full
            else:
                col_count = col_iter
                grid[row_count][col_iter] += grid[row_count][col_count]
                grid[row_count][col_count] = 0

                if col_iter == col - 1:
                    row_count += 
