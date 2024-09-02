
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
    from collections import deque
    def max_fill_helper(grid, capacity, height, result):
        if height >= len(grid):
            return result
        acc = 0
        for i in range(height, len(grid)):
            if grid[i][0] == 0:
                break
            acc += grid[i][0]
            if acc > capacity:
                return max_fill_helper(grid, capacity, i, result + 1)
        return max_fill_helper(grid, capacity, height + 1, result)
    max_height = len(grid) - 1
    max_grid = [[0 for _ in range(len(grid[0]))] for _ in range(max_height + 1)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                continue
            max_grid[max_height][j] = max(max_grid[max_height][j], grid[i][j])
    return max_fill_helper(max_grid, capacity, 0, 0)

