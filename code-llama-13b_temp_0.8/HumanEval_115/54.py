
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
    
    def bucket_fill(grid, start, capacity):
        if capacity == 0: return 0
        if grid[start[0]][start[1]] == 0: return 0
        max_fill = 0
        rows = len(grid)
        columns = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            x, y = start[0] + direction[0], start[1] + direction[1]
            if not 0 <= x < rows or not 0 <= y < columns: continue
            new_capacity = capacity
            if grid[x][y] == 0: continue
            while new_capacity > 0:
                grid[x][y] -= 1
                max_fill += 1
                new_capacity -= 1
                next_fill = bucket_fill(grid, (x, y), new_capacity)
                max_fill += next_fill
                new_capacity += next_fill
                grid[x][y] += 1
        return max_fill
    
    max_fills = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_fills += bucket_fill(grid, (i, j), capacity)
    return max_fills


