
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
    height, length = len(grid), len(grid[0])
    level = [[-1 for _ in range(length)] for _ in range(height)]
    level[height-1][0] = grid[height-1][0]
    # print(level)

    for i in range(height-2, -1, -1):
        for j in range(length):
            level[i][j] = min(level[i+1][j], level[i+1][j-1]) + grid[i][j]
            if level[i][j] > capacity:
                return math.inf
            # print(level[i][j], capacity)
    # print(level)
    return sum([i == capacity for row in level for i in row])

