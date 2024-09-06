
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
    capacity_grid = [[0] * (grid.shape[0] + 1) for _ in range(grid.shape[1])]
    for row in grid:
        capacity_grid[row[1]][0] = capacity
    for row in grid:
        for column in range(1, row[1]):
            capacity_grid[row[1]][column] = max(capacity_grid[row[1]][column], capacity_grid[row[1]-1][column])
    for row in reversed(grid):
        for column in range(1, row[1]):
            capacity_grid[row[1]][column] = max(capacity_grid[row[1]][column], capacity_grid[row[1]-1][column])
    for row in grid:
        result = 0
        for column in range(1, row[1]):
            if grid[row][1] == 1:
                if capacity_grid[row[1]][column] == 0:
                    result += 1
            if capacity_grid[row[1]][column] > 0:
                if capacity_grid[row[1]][column] <= grid[row][0]:
                    result += 1
        print(result)
        
grid = [
[0,0,1,0],
[0,1,0,0],
[1,1,1,1],
[0,0,1,1],
[0,1,0,0],
[1,1,1,0],
[0,0,1,0],
[0,0,0,0],
[1,1,1,1],
[0,1,1,1],
[0,0,1,0],
[1,1,1,0],
[0,0,1,1],
[0,1,1,0],
[1,1,1,1],
[0,0,0,0],
[1,1,1,1],
[0,1,1,1],
[0,0,0,0],
[1,1,1,1]
]

grid = max_
