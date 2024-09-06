
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
    # TODO: Write your code here
    #time complexity O(n^3)
    #space complexity O(n)
    n = len(grid)
    m = len(grid[0])
    dp = [[-1 for j in range(n)] for i in range(n)]

    def helper(row,col,level):
        if level==n:
            return 0
        if dp[row][col]!=-1:
            return dp[row][col]
        if grid[row][col]==1:
            dp[row][col]=math.inf
            min_moves=min(helper(row-1,col,level+1),helper(row+1,col,level+1),helper(row,col-1,level+1),helper(row,col+1,level+1))+level
            dp[row][col]=min_moves
            return min_moves
        else:
            return helper(row,col,level+1)
        
    min_moves=helper(0,0,0)
    if min_moves==math.inf:
        min_moves=0
    return min_moves
