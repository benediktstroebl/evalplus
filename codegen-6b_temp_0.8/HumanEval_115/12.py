
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
    # Inspired by: http://www.geeksforgeeks.org/shortest-time-to-fill-the-buckets/

    # keep track of maximum capacity per column
    mn = [max(row[:capacity]) for row in grid]
    # capacity-1 because we want width to us length
    mn = [row[capacity-1:] for row in grid]
    if min(mn) == 0:
        return 0
    # now we need to populate the buckets
    # we need to find the smallest column that has a bucket above capacity, and
    # for each row, we can use the smallest column with a bucket above capacity
    # to remove that column
    # we also need to lower the capacity of that column to 0
    i = mn.index(min(mn))
    for row in grid:
        while min(row[i:]) > 0:
            row[i] -= 1
            i += 1
    return len(grid) - i - 1

