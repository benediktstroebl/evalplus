
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
    
    R, C = len(grid), len(grid[0])
    #print(R, C)
    #print(grid)
    
    # count the number of 1s in each row
    col_counts = []
    for row in grid:
        col_counts.append(row.count(1))
    
    # print(col_counts)
    
    # store a boolean array of whether each column is
    # possible to get to zero
    possible = [False] * C
    
    # find the longest chain of 1s
    longest_chain = max(col_counts)
    
    # count the number of 1s in each row
    row_counts = []
    for i in range(R):
        row_counts.append(grid[i].count(1))
    
    # find the row with the shortest length
    shortest_row = min(row_counts)
    
    # loop through all the rows
    for i in range(R):
        if col_counts[i] == 0:
