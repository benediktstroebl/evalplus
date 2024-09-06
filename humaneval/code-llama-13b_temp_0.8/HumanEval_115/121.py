
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
    def fill_row(row, capacity):
        count = 0
        bucket_start = 0
        bucket_end = 0
        while bucket_end < len(row):
            if row[bucket_end] == 1:
                count += 1
            bucket_end += 1
            if count == capacity:
                return bucket_end
        return bucket_end
    
    def fill_grid(grid, capacity, bucket_start, bucket_end):
        count = 0
        for i in range(bucket_start, bucket_end):
            count += fill_row(grid[i], capacity)
        return count

    max_length = len(grid)
    bucket_end = 0
    while bucket_end < max_length:
        bucket_start = bucket_end
        bucket_end = fill_grid(grid, capacity, bucket_start, max_length)
        if bucket_end == max_length:
            return count + (max_length - bucket_start)
        if math.ceil((bucket_end - bucket_start) / 2) >= capacity:
            bucket_end = bucket_start + math.ceil((bucket_end - bucket_start) / 2)
            count += 1
    return count

