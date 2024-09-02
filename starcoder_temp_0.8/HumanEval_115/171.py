
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
    rows = len(grid)
    cols = len(grid[0])

    # Get the indices of all the 1s
    ones = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                ones.append((i, j))
    
    # There are two cases:
    # 1. (i, j) is in a bucket: we can get water by emptying the bucket
    # 2. (i, j) is not in a bucket: we can get water by connecting to the bucket
    
    # We can do DFS to get all the connected buckets
    # Once we've done DFS, we need to calculate the maximum number of times we need to empty buckets
    # to get all the water from all the wells

    # We can do a DFS for every 1. We keep a variable to keep track of the depth and a variable to
    # check if we've seen a 1 before.
    # We need to make sure the depth is not 0 since the start position is a 1.
    # We also need to make sure we haven't seen the 1 before, since if we have seen a 1 before,
    # that means the depth of this node is 2. We return 1 since we need to empty the bucket.
    # If we haven't seen the 1 before, we can just calculate the number of times we need to empty
    # the bucket to get water by DFS.

    # We need to track the number of times we need to empty buckets
    # We can calculate this by doing a DFS on all the 1s. We keep a variable to keep track of the depth and a variable to
    # check if we've seen a 1 before.
    # We need to make sure the depth is not 0 since the start position is a 1.
    # We also need to make sure we haven't seen the 1 before, since if we have seen a 1 before,
    # that means the depth of this node is 2. We return 1 since we need to empty the bucket.
    # If we haven't seen the 1 before, we can just calculate the number of times we need to empty
    # the bucket to get water by DFS.

    ans = 0
    for (i, j) in ones:
        ans += empty(grid, i, j, capacity, {})
   
