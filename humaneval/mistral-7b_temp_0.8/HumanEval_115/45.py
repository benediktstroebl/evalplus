
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
    N, M = len(grid), len(grid[0])
    dp = [(0,0)]*(N+1)
    for i in range(1, N+1):
        for j in range(1, M+1):
            for k in range(1, min(i+1, M)+1):
                dp[i][j] = max(dp[i][j], max(dp[i][j-k]+k, dp[i-k][j]+k), dp[i-k][j-k])
    return dp[-1][-1]

    # O(N*M*B) time | O(N*M) space

    # Backtracking:
    # Time: O(N^3)
    # Space: O(N^3)

    def is_possible(grid, capacity):
        for row in grid:
            for num in row:
                if num > capacity:
                    return False
        return True

    def bucket_filling(grid, capacity, bucket_num=0):
        if bucket_num == len
