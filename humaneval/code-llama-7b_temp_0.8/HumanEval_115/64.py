
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
    def get_min(grid, x, y, capacity, visited):
        if not is_valid(grid, x, y) or not is_empty(grid, x, y) or (x, y) in visited:
            return math.inf

        n = len(grid)
        m = len(grid[0])

        count = 0
        used = 0
        visited.add((x, y))

        for i in range(x, n):
            for j in range(y, m):
                if grid[i][j] == 0:
                    continue
                count += 1
                used += grid[i][j]
                if used > capacity:
                    return count
            used = 0
        
        for j in range(y, m):
            for i in range(x, n):
                if grid[i][j] == 0:
                    continue
                count += 1
                used += grid[i][j]
                if used > capacity:
                    return count
            used = 0

        return count

    def is_valid(grid, x, y):
        n = len(grid)
        m = len(grid[0])
        return (0 <= x and x < n) and (0 <= y and y < m)

    def is_empty(grid, x, y):
        return grid[x][y] == 0

    if capacity == 0:
        return 0
    
    n = len(grid)
    m = len(grid[0])
    visited = set()
    ans = math.inf

    for i in range(n):
        for j in range(m):
            if (i, j) in visited:
                continue
            else:
                ans = min(ans, get_min(grid, i, j, capacity, visited))

    return ans
