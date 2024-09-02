
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
    import math
    # [2, 1, 1, 2], [1, 2, 1, 1], [2, 2, 2, 3]
    # [1, 1, 2, 1], [0, 1, 1, 0], [1, 1, 1, 1], [0, 1, 1, 1]

    grid = grid[::-1]
    capacity = int(capacity)

    length = len(grid[0])
    height = len(grid)

    def get_water_level(row):
        return sum(row)

    def can_hold(row, bucket):
        return row - bucket >= 0

    def can_hold_max_water(row, bucket):
        return row - bucket >= bucket

    def get_max_water(capacity, length):
        return capacity * length

    # O(n^3) time | O(n^2) space
    # def max_fill(grid, capacity):
    #     # # Initialize local variables
    #     # num_buckets = len(grid)
    #     # num_wells = len(grid[0])
    #     # total_water_level = 0

    #     # for row in range(num_buckets):
    #     #     for col in range(num_wells):
    #     #         current_row = grid[row]
    #     #         current_well_level = current_row[col]
    #     #         current_bucket_capacity = capacity

    #     #         # Check to see if the current well has water
    #     #         if current_well_level > 0:
    #     #             # Check to see if the current well has enough water to fill the bucket
    #     #             if can_hold(current_well_level, current_bucket_capacity):
    #     #                 total_water_level += current_well_level
    #     #             else:
    #     #                 # Reduce the bucket capacity until the current well can be filled
    #     #                 current_bucket_capacity
