
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
    def dfs(row, column, bucket_index, capacity):
        if row < 0 or row >= grid.length or column < 0 or column >= grid[row][column].length or grid[row][column] == 0:
            return
        if grid[row][column] == 1:
            if capacity == 0:
                return
            else:
                bucket_index = max(bucket_index - 1, 0)
                if not dfs(row, column, bucket_index, capacity - grid[row][column]):
                    return
        for i in range(4):
            for j in range(4):
                if (row + i, column + j) not in [ (0,0),(0,1),(1,1),(1,0) ] and \
                   grid[row + i][column + j] == 1 and \
                   capacity > grid[row + i][column + j]:
                    capacity = grid[row + i][column + j]
                    dfs(row + i, column + j, bucket_index, capacity)
    return dfs(0, 0, 0, capacity)
