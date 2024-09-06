
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
    def dfs(grid, i, j, capacity, path):
        """
        Depth first search
        """
        if grid[i][j] == 1:
            grid[i][j] = 0
            path.append((i, j))
            dfs(grid, i+1, j, capacity, path)
            dfs(grid, i-1, j, capacity, path)
            dfs(grid, i, j+1, capacity, path)
            dfs(grid, i, j-1, capacity, path)
        elif grid[i][j] == 0:
            return
        else:
            return
    
    def mark(grid, i, j):
        """
        Marks the well
        """
        if grid[i][j] == 0:
            grid[i][j] = 1
        for row in range(grid.shape[0]):
            for col in range(grid.shape[1]):
                if row != i or col != j:
                    mark(grid, row, col)
        
    path = []
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            mark(grid, i, j)
            capacity_needed = max(0, capacity - (grid[i][j] - 1))
            dfs(grid, i, j, capacity_needed, path)
    
    return len(path)