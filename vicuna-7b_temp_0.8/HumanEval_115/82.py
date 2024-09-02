
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
    buckets = [0] * (cols * 2 + 1)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                bucket = buckets[col / 2]
                buckets[col / 2] -= 1
                for _ in range(int(grid[row][col] ** 2 * bucket_capacity / bucket)):
                    if int(grid[row][col]) > 1:
                        break
                else:
                    for _ in range(int(grid[row][col] ** 2 * bucket_capacity / bucket - 1)):
                        if int(grid[row][col]) > 1:
                            break
                    else:
                        buckets[col / 2] += 1
    return len(buckets)