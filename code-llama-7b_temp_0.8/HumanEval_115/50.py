
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
    # Memoize
    import sys
    memo = {}
    def dfs(x, y, capacity):
        # If there is no water
        if grid[x][y] == 0:
            # If the bucket is filled
            if capacity == 0:
                return 0
            else:
                return sys.maxsize

        # If the bucket is full
        if capacity == 1:
            return 1

        if (x, y, capacity) in memo:
            return memo[(x, y, capacity)]

        ans = float('inf')

        # We have two options: We can take the water from the current well
        # or we can go to the next well
        #
        # If we go to the next well we take the water from there
        ans = dfs(x + 1, y, capacity - grid[x][y])

        # If we take the water from the current well
        # we go to the next well
        ans = min(ans, dfs(x + 1, y + 1, capacity))

        memo[(x, y, capacity)] = ans
        return ans

    return dfs(0, 0, capacity)


