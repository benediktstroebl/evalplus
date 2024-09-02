
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
    # Finding the number of wells
    n,m = len(grid),len(grid[0])
    # Finding the number of buckets
    k = capacity
    # Finding the number of buckets needed to empty all the wells
    total_buckets = 0
    # Iterating through each row in the grid
    for i in range(n):
        # Iterating through each column in the grid
        for j in range(m):
            # If the cell is 1
            if grid[i][j] == 1:
                # We use a binary search to find the number of buckets needed to empty the well
                lower = 0
                upper = k
                while lower <= upper:
                    # We get the middle value of the binary search
                    mid = (lower + upper) // 2
                    # We check if the middle value can empty the well
                    if can_empty(grid,i,j,mid):
                        # If the middle value can empty the well, we use the middle value
                        lower = mid + 1
                
