
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
    # Initialize empty lists to store the number of times each bucket is used
    used_buckets = [[0] * (capacity+1) for _ in range(len(grid))]
    empty_buckets = [[0] * (capacity+1) for _ in range(len(grid))]
    for row in grid:
        # If a well is completely empty, fill it with water
        if not row:
            for bucket in used_buckets:
                bucket[row[0]] += 1
                used_buckets[row[0]][bucket-1] = 0
        # If a well is partially filled, empty it and fill the remaining space with water
        else:
            for bucket in empty_buckets:
                if bucket <= row[1]:
                    bucket -= 1
                    empty_buckets[row[0]][bucket] = 0
            for i in range(1, capacity+1):
                if row[1] < i and row[1] in used_buckets[0]:
                    used_buckets[row[0]][i-1] += 1
                else:
                    used_buckets[row[0]][i-1] = 1
    
    return max(used_buckets)