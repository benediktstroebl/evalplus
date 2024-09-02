
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
    rows, cols = grid.shape
    row_sums = [0] * rows
    col_sums = [0] * cols

    for row in range(rows):
        row_sum = 0
        for col in range(cols):
            if grid[row][col] == 1:
                row_sum += bucket_capacity
            else:
                col_sum += bucket_capacity

        max_diff = max(abs(row_sum - col_sum))
        max_fills = max_diff + 1
        for i in range(max_fills):
            for col in range(cols):
                if grid[row][col] == 1:
                    row_sum -= bucket_capacity
                    col_sum += bucket_capacity
                    if row_sum > 0:
                        break
                else:
                    col_sum -= bucket_capacity
                    row_sum += bucket_capacity
                    if col_sum > 0:
                        break
            if row_sum <= 0:
                break
        row_sums[row] = row_sum
        col_sums[row] = col_sum

    return max_fills