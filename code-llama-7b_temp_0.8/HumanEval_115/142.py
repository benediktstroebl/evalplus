
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
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    row_len = len(grid[0])
    total_len = len(grid) * row_len
    buckets = 1

    # find total amount of water
    for i in range(len(grid)):
        for j in range(row_len):
            if grid[i][j] == 1:
                total_len -= 1

    # find how many buckets are needed
    buckets = math.ceil(total_len / capacity)

    # find how many times we need to empty buckets
    for i in range(row_len):
        curr_filled = 0
        for j in range(len(grid)):
            if grid[j][i] == 1:
                curr_filled += 1
            if curr_filled == capacity:
                curr_filled -= 1
                buckets -= 1
            elif curr_filled < capacity:
                break
    return buckets
