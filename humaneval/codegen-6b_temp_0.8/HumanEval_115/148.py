
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
    import math
    m, n = len(grid), len(grid[0])
    assert all(len(row) == n for row in grid)
    count, capacity = 0, math.floor(capacity)
    while True:
        total = sum(grid[i][j] for i in range(m) for j in range(n) if grid[i][j])
        if total == 0:
            return count
        if total < capacity:
            capacity -= total
            count += 1
        else:
            n_row = m - 1
            for i in range(m - 1, -1, -1):
                while grid[i][n_row] == 0 and n_row >= 0:
                    n_row -= 1
                if grid[i][n_row] < capacity:
                    capacity -= grid[i][n_row]
                    grid[i][n_row] = 0
                    count += 1
                else:
                    grid[i][n_row] -= capacity
                    capacity = 0
                    break
