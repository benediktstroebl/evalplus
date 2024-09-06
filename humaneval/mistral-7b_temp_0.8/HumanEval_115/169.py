
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
    w, h = len(grid), len(grid[0])

    stack = [(0, 0, 1)]
    count = 0

    while stack:
        i, j, water = stack.pop()
        count += 1

        if water >= capacity:
            continue

        if i == w:
            continue

        if j < h-1:
            stack.append((i, j+1, water+grid[i][j+1]))

        if j > 0:
            stack.append((i, j-1, water+grid[i][j-1]))

        if i > 0:
            stack.append((i-1, j, water+grid[i-1][j]))

    return count
