
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
    def find_min_max_val(grid):
        rows , cols = len(grid), len(grid[0])
        min_val, max_val = float('inf'), -float('inf')
        for row in range(rows):
            for col in range(cols):
                val = grid[row][col]
                min_val = min(min_val, val)
                max_val = max(max_val, val)
        return min_val, max_val

    min_val, max_val = find_min_max_val(grid)
    res = 0
    while min_val <= max_val:
        mid = (min_val + max_val) / 2
        bucket_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] != 0:
                    #print("bucket_count = %d\tin row = %d, col = %d" % (bucket_count, row, col))
                    bucket_count += math.ceil(grid[row][col]/mid)
        #print("bucket_count = %d, min_val = %d, mid = %d" % (bucket_count, min_val, mid))
        if bucket_count <= capacity:
            res += 1
            min_val = mid + 1
        else:
            max_val = mid - 1
    return res
                
