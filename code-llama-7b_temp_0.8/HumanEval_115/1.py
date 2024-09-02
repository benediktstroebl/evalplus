
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
    def count_used(grid):
        return sum([len(row) for row in grid])

    def count_available(grid):
        return len(grid[0]) - count_used(grid)

    def total_available(grid):
        return len(grid) * len(grid[0]) - count_used(grid)

    buckets_used = 0
    # While there are still wells left to empty
    while count_used(grid) < len(grid) * len(grid[0]):
        # add 1 to the number of buckets used
        buckets_used += 1
        # Find all wells that can be emptied
        wells_to_empty = []
        for well in range(len(grid[0])):
            if grid[0][well] == 1:
                wells_to_empty.append(well)
        # Find the minimum number of wells to empty
        minimum_wells = min(total_available(grid), len(wells_to_empty))
        # empty that number of wells
        for well in range(minimum_wells):
            grid[wells_to_empty[well]][well] = 0

    return buckets_used

