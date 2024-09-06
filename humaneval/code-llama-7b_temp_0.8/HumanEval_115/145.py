
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
    # idea: treat grid as a single array, which we can use to fill up buckets
    # however, we are filling buckets up in the order of left -> right,
    # and left -> right is the same as row -> column

    # extract all elements from grid and store them in an array
    flat_list = []
    for row in grid:
        for col in row:
            flat_list.append(col)

    # calculate how many elements we need to extract from the array
    # and how many buckets we have to extract them with
    total_extracted = 0
    num_buckets = math.ceil(len(flat_list) / capacity)
    while total_extracted < len(flat_list):
        for i in range(num_buckets):
            if total_extracted + capacity > len(flat_list):
                total_extracted += len(flat_list) - total_extracted
                break
            total_extracted += capacity
        if total_extracted < len(flat_list):
            num_buckets += 1

    return num_buckets
