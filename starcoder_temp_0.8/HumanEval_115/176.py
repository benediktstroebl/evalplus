
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
    # TODO: Linear time algo 
    n_rows, n_cols = len(grid), len(grid[0])
    top_left = [0]
    bot_right = [0]
    for i in range(n_rows):
        for j in range(n_cols):
            if i > 0:
                top_left.append(top_left[-1] + grid[i][j])
            else:
                top_left.append(grid[i][j])

    for i in range(n_cols - 1, -1, -1):
        bot_right.append(bot_right[-1] + grid[n_rows - 1][i])

    print(top_left)
    print(bot_right)
    # TODO: Count max bucket usage
