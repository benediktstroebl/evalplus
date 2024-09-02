
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
    import itertools
    import math

    def bucket_loop(grid, capacity):
        def loop(grid, capacity, index, val):
            if index == len(grid[0]):
                return 0
            if grid[val][index] == 0:
                return loop(grid, capacity, index + 1, val)
            for i in range(len(grid)):
                if i != val:
                    loop(grid, capacity, index, i)

        def reduce_loop(grid):
            def loop(grid, capacity, index, val):
                if index == len(grid[0]):
                    return 0
                if grid[val][index] == 0:
                    return loop(grid, capacity, index + 1, val)
                for i in range(len(grid[0])):
                    if i != val:
                        loop(grid, capacity, index, i)
            reduced = [row.copy() for row in grid]
            loop(reduced, capacity, 0, 0)
            return reduced

        def check_all_zero(grid):
            for row in grid:
                for val in row:
                    if val != 0:
                        return False
            return True

        grid = reduce_loop(grid)
        if check_all_zero(grid):
            return 0
        water_cnt = 0
        for row in grid:
            for val in row:
                if val == 0:
                    water_cnt += 1
                else:
                    break
        return sum([math.ceil(water_cnt / capacity)])

    # Calculate the total number of well cells
    well_cnt = 0
    for row in grid:
        well_cnt += row.count(1)
    # Calculate the number of cycles to fill all wells
    cycles = 0
    for row in grid:
        for val in row:
            if val != 0:
                break
        else:
            cycles += 1
    cycles *= well_cnt
    # Calculate the number of cycles to fill the wells
    cycles = int(math.ceil(capacity * cycles / well_cnt))
    return cycles
