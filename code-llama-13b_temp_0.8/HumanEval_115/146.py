
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
    def get_max_sum_for_row(row, capacity, bucket_sum):
        """
        Find the highest number of buckets you can fill with the remaining capacity
        """
        # The highest number of buckets you can fill with the remaining capacity
        buckets = min(capacity, len(row))
        # The sum of buckets filled
        bucket_sum += buckets
        # Remove filled buckets from the capacity
        capacity -= buckets
        # Remove filled buckets from the grid
        row = row[buckets:]
        return bucket_sum, capacity, row

    def find_max_sum_for_grid(grid, capacity):
        """
        Find the max sum of buckets that can be filled
        """
        # The max sum of buckets that can be filled
        bucket_sum = 0
        # The remaining capacity of the buckets
        capacity = capacity
        for row in grid:
            # Find the highest number of buckets you can fill with the remaining capacity
            bucket_sum, capacity, row = get_max_sum_for_row(row, capacity, bucket_sum)
            # If there is not enough space for the current bucket
            while capacity < len(row):
                # Remove the top bucket from the row
                row = row[1:]
                # Find the highest number of buckets you can fill with the remaining capacity
                bucket_sum, capacity, row = get_max_sum_for_row(row, capacity, bucket_sum)
        return bucket_sum

    # Find the max sum of buckets that can be filled
    max_sum = find_max_sum_for_grid(grid, capacity)
    # Find the number of times you need to lower the buckets
    lower_buckets = math.ceil(sum(map(sum, grid)) / capacity)
    # Return the number of times you need to lower the buckets
    return lower_buckets - max_sum

