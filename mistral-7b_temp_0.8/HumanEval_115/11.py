
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
    # dfs solution
    height, width = len(grid), len(grid[0])
    stack = []
    visited = set()
    # dfs from the bottom-rightmost cell
    stack.append((height-1, width-1))
    ans = 0
    while stack:
        row, col = stack.pop()
        if (row, col) in visited: continue
        visited.add((row, col))
        if row > 0 and grid[row-1][col] == 1:
            # add the current cell and the cells above it to the stack
            stack.extend([(row-1, col), (row-1, col+1), (row-1, col-1)])
        if col > 0 and grid[row][col-1] == 1:
            stack.extend([(row, col-1), (row+1, col-1), (row-1, col-1)])
        if row < height-1 and grid[row+1][col] == 1:
            stack.extend([(row+1, col), (row
