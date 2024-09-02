
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

    num_rows = len(grid)
    num_cols = len(grid[0])

    # Initiate result variable
    max_open_buckets = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 1:
                # Find number of open buckets (vertical)
                num_open_buckets = 1
                for r in range(row + 1, num_rows):
                    if grid[r][col] == 1:
                        num_open_buckets += 1
                    else:
                        break
                
                # Find number of open buckets (horizontal)
                for c in range(col + 1, num_cols):
                    if grid[row][c] == 1:
                        num_open_buckets += 1
                    else:
                        break

                # Find max num open buckets
                max_open_buckets = max(max_open_buckets, num_open_buckets)

    return math.ceil(max_open_buckets / capacity)

