
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
    # let's say that the water is located at the left side
    # of the well; we'll remove it
    # if we eventually end up with an empty grid
    # that means we'll need to remove one unit of water
    # from the well
    
    # the grid is a square: (len(grid) == len(grid[0]))
    # and the size of each well is the same
    rows = len(grid)
    cols = len(grid[0])
    
    buckets = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            buckets[i][j] = grid[i][j]
    
    # let's start with the right most column
    curr_col = cols - 1
    for i in range(rows - 1, -1, -1):
        # we'll keep track of the last bucket that was emptied
        last_bucket_idx = -1
        curr_row = i
        
        while buckets[curr_row][curr_col] != 0:
            # now we want to find the smallest bucket index that is past the 
            # current bucket
            for j in range(curr_row, rows):
                if buckets[j][curr_col] == 0:
                    curr_row = j
                    last_bucket_idx = j
                    break
            
            # extract water
            curr_row_water = math.floor(capacity / buckets[curr_row][curr_col])
            buckets[curr_row][curr_col] -= curr_row_water
            if buckets[curr_row][curr_col] == 0:
                last_bucket_idx = curr_row
            
            # move on to next column
            curr_col -= 1
            
            if curr_col == -1:
                curr_col = cols - 1
        
        # now we need to locate the last bucket that was emptied
        while last_bucket_idx >= 0:
            # now we want to empty this bucket
            # and we also