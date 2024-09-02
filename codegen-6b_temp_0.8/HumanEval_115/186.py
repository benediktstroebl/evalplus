
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
    n = len(grid)
    m = len(grid[0])
    
    visited = [[False] * n for _ in range(m)]
    def helper(grid, visited, row, col, capacity, count):
        if capacity < 0:
            return False, count
        if row < 0 or row >= n or col < 0 or col >= m:
            return False, count
        if visited[row][col]:
            return False, count
        if grid[row][col] == 0:
            return False, count
        visited[row][col] = True
        count += 1
        count = helper(grid, visited, row + 1, col, capacity - grid[row][col], count)
        count = helper(grid, visited, row - 1, col, capacity - grid[row][col], count)
        count = helper(grid, visited, row, col + 1, capacity - grid[row][col], count)
        count = helper(grid, visited, row, col - 1, capacity - grid[row][col], count)
        visited[row][col] = False
        return True, count

    for row in range(n):
        for col in range(m):
            _, count = helper(grid, visited, row, col, capacity, 0)
            if count > 0:
                return count
    return 0

assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6
assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 2) == 5
assert max_fill([[0,0,0], [0,0,0]], 5) == 0
assert max_fill([[0,0,0], [0,0,0]], 1) == 0
assert max_fill([[0,0,0], [0,0,0], [0,0,0]], 1) == 0
assert max_fill([[0,0,2,0], [1,1,1,1], [2,0,0,1]], 7) == 4
