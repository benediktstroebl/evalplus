
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
    # TODO: WIP
    # def max_fill(grid, capacity):
    #     def move_all_to_left(buckets, wells):
    #         import math
    #         # current_bucket = 0
    #         # move_all_to_left_per_bucket(buckets, wells, current_bucket)

    #         # for bucket in range(1, len(buckets)):
    #         #     move_all_to_left_per_bucket(buckets, wells, bucket)
    #         # return buckets, wells

    #         # def move_all_to_left_per_bucket(buckets, wells, current_bucket):
    #         #     for well in range(0, len(wells)):
    #         #         while wells[well] >= buckets[current_bucket]:
    #         #             wells[well] -= buckets[current_bucket]
    #         #             buckets[current_bucket] += buckets[current_bucket]

    #         #         # wells[well] -= buckets[current_bucket]
    #         #         # buckets[current_bucket] += buckets[current_bucket]
    #         #         # wells[well] -= buckets[current_bucket]

    #         #     buckets[current_bucket] = math.floor(buckets[current_bucket] / 2)

    #     buckets = [capacity for _ in range(len(grid))]
    #     wells = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    #     move_all_to_left(buckets, wells)

    #     return sum(buckets)

    # return max_fill(grid, capacity)
    def max_fill(grid, capacity):
        def move_all_to_left(buckets, wells):
            # current_bucket = 0
            # move_all_to_left_per_bucket(buckets, wells, current_bucket)

            # for bucket in range(1, len(buckets)):
            #     move
