
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
    # grid : [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    # bucket_capacity : 2
    # Output: 5
    def get_row_len(grid):
        return len(grid[0])

    def get_row_count(grid):
        return len(grid)

    def get_wells(grid):
        wells = []
        for i, row in enumerate(grid):
            wells.append(sum(row))
        return wells

    def get_wells_with_index(grid):
        wells = []
        for i, row in enumerate(grid):
            wells.append([sum(row), i])
        return wells

    def get_buckets(capacity):
        buckets = []
        for i in range(capacity):
            buckets.append(0)
        return buckets

    def get_max_bucket(buckets):
        return max(buckets)

    def get_empty_bucket_count(buckets):
        count = 0
        for bucket in buckets:
            if bucket == 0:
                count += 1
        return count

    def lower_buckets(buckets, capacity):
        buckets_to_lower = 0
        for bucket in buckets:
            if bucket < capacity:
                buckets_to_lower += 1
        return buckets_to_lower

    def get_bucket_count(buckets, wells):
        count = 0
        for i in range(len(wells)):
            if wells[i] >= capacity:
                count += 1
        return count

    def add_buckets(buckets, wells):
        for i in range(len(wells)):
            if wells[i] >= capacity:
                buckets[i] += wells[i]
                wells[i] -= capacity
        return wells

    def print_grid(grid):
        for i, row in enumerate(grid):
            print(row)

    # -
