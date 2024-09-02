
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
    def helper(grid, capacity, m, n, i, j, cur_capacity, cur_count):
        if cur_count == 0:
            return cur_capacity
        
        up = (i-1,j)
        down = (i+1,j)
        left = (i,j-1)
        right = (i,j+1)
        if up[0] >= 0 and grid[up[0]][up[1]] == 1:
            grid[up[0]][up[1]] = 0
            grid[i][j] = 0
            cur_capacity = min(cur_capacity, capacity-1)
            cur_count -= 1
            return helper(grid, capacity, m, n, up[0], up[1], cur_capacity, cur_count)
        elif down[0] < m and grid[down[0]][down[1]] == 1:
            grid[down[0]][down[1]] = 0
            grid[i][j] = 0
            cur_capacity = min(cur_capacity, capacity-1)
            cur_count -= 1
            return helper(grid, capacity, m, n, down[0], down[1], cur_capacity, cur_count)
        elif left[1] >= 0 and grid[left[0]][left[1]] == 1:
            grid[left[0]][left[1]] = 0
            grid[i][j] = 0
            cur_capacity = min(cur_capacity, capacity-1)
            cur_count -= 1
            return helper(grid, capacity, m, n, left[0], left[1], cur_capacity, cur_count)
        elif right[1] < n and grid[right[0]][right[1]] == 1:
            grid[right[0]][right[1]] = 0
            grid[i][j] = 0
            cur_capacity = min(cur_capacity, capacity-1)
            cur_count -= 1
            return helper(grid, capacity, m, n, right[0], right[1], cur_capacity, cur_count)
        else:
            return cur_capacity
    
    max_buckets = -math.inf
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[
