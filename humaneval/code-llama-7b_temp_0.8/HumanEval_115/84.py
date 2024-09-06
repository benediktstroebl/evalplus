
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
    def find_row_w_water(grid, bucket_capacity):
        """
        Given a grid of 0s and 1s, find a row with water. 
        If none found, return -1
        """
        for i in range(len(grid)):
            if sum(grid[i]) > 0:
                return i
        return -1

    def find_bucket_capacity(grid):
        return max(max(row) for row in grid)

    if len(grid) == 0:
        return 0

    # Determine bucket capacity
    bucket_capacity = find_bucket_capacity(grid)

    # Initialize variables
    buckets = [0] * len(grid)
    times_lowered = 0
    empty_wells = 0

    # While wells still have water
    while empty_wells != len(grid):
        times_lowered += 1

        # Find first row with water
        row_index = find_row_w_water(grid, bucket_capacity)

        # If no water left, break
        if row_index == -1:
            break

        # Find how much water is in this row
        water_in_row = sum(grid[row_index])

        # Adjust bucket counts
        for i in range(len(grid[0])):
            if grid[row_index][i] == 1:
                buckets[i] += 1
            elif buckets[i] > 0:
                buckets[i] -= 1

        # Determine how much water we can extract
        extracted_water = min(bucket_capacity, buckets[row_index])

        # Update how much water is left in row
        grid[row_index][row_index] = max(0, water_in_row - extracted_water)

        # If all wells are empty, break
        empty_wells = sum(grid[row_index])

    return times_lowered

