
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
    n = len(grid[0])
    m = len(grid)

    # Fill the left-most column (0th column)
    for i in range(1, m):
        grid[i][0] += grid[i - 1][0]

    # Fill the remaining columns
    for j in range(1, n):
        for i in range(m - 1, -1, -1):
            grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])

    # Find the maximum area
    ans = grid[m - 1][n - 1]

    # Try removing one well and then find the maximum area
    for i in range(m):
        for j in range(n):
            # Check if we can remove the well
            if grid[i][j] - grid[i - 1][j] > capacity:
                continue

            # Remove the well and then find the maximum area
            ans = max(ans, find_max(grid, m, n, i, j, capacity))

    return ans

