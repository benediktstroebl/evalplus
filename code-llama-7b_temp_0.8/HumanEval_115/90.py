
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

    def get_water_in_bucket(bucket):
        return sum(bucket)

    def is_bucket_full(bucket):
        return get_water_in_bucket(bucket) >= capacity

    def move_water_down(grid, bucket, row, col):
        if is_bucket_full(bucket):
            return
        if row == 0 and get_water_in_bucket(bucket) > 0:
            return

        top_bucket = grid[row - 1][col]
        bucket[0] += top_bucket

        if is_bucket_full(bucket):
            grid[row - 1][col] = 0
            move_water_down(grid, bucket, row - 1, col)

        bucket[0] -= top_bucket

        top_water_in_bucket = grid[row][col - 1]
        grid[row][col - 1] = 0
        bucket[0] += top_water_in_bucket
        grid[row][col] = 0

        if is_bucket_full(bucket):
            move_water_down(grid, bucket, row, col - 1)
        bucket[0] -= top_water_in_bucket

    grid_height, grid_width = len(grid), len(grid[0])
    total_moves = 0
    for row in range(grid_height):
        for col in range(grid_width):
            bucket = [0]
            if grid[row][col] > 0:
                grid[row][col] -= 1
                move_water_down(grid, bucket, row, col)
                if bucket[0] > 0:
                    total_moves += math.ceil(bucket[0] / capacity)
    return total_moves

