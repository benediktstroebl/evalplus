
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
    rows = len(grid)
    cols = len(grid[0])

    # Create DP table.
    # rows: number of wells, cols: number of buckets
    table = [[math.inf for _ in range(capacity+1)] for _ in range(rows+1)]

    # Populate DP table.
    for i in range(rows):
        for j in range(capacity+1):
            # Bucket is empty (can be filled).
            if j == 0:
                table[i+1][j] = 0
            # Bucket is not empty (can't be filled).
            elif grid[i][j-1] == 1:
                table[i+1][j] = table[i][j]
            # Bucket can be filled.
            elif grid[i][j-1] == 0:
                table[i+1][j] = min(table[i][j], table[i][j-1] + 1)

    # Count number of times table is modified.
    count = 0
    for i in range(rows):
        for j in range(capacity):
            # Bucket is empty.
            if table[i+1][j] == 0:
                count += 1
            # Bucket is not empty.
            else:
                table[i+1][j] = min(table[i+1][j], table[i][j] - 1)

    return count

