
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
    def get_bucket_count(row_size):
        return math.ceil(row_size / capacity)

    def get_buckets_for_row(row_size):
        bucket_count = get_bucket_count(row_size)
        if bucket_count == 1:
            return [(row_size, 0)]

        buckets = []
        for index in range(bucket_count):
            start = index * capacity
            end = min(start + capacity, row_size)
            buckets.append((end - start, start))
        return buckets

    def get_water_count(row_with_buckets):
        water_count = 0
        for row in row_with_buckets:
            if row[0] > 0:
                water_count += row[0]
        return water_count

    def get_row_with_buckets(row):
        water_count = get_water_count(row)
        if water_count <= capacity:
            return row

        buckets = get_buckets_for_row(water_count)
        row_with_buckets = []
        for bucket in buckets:
            row_with_buckets.append((bucket[0], row[bucket[1]]))
        return row_with_buckets

    water_count = 0
    bucket_count = 0
    for row in grid:
        row_with_buckets = get_row_with_buckets(row)
        water_count += get_water_count(row_with_buckets)
        bucket_count += get_bucket_count(len(row))

    return water_count // capacity + bucket_count

