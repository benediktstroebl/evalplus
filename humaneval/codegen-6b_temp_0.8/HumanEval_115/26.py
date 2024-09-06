
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
    rows = len(grid)
    cols = len(grid[0])

    wells = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0:
                wells.append((r, c))

    def is_less_than_capacity(total_water):
        for well in wells:
            well_water = grid[well[0]][well[1]]
            if well_water >= total_water:
                return False
        return True

    def has_space(capacity):
        if is_less_than_capacity(capacity):
            return True
        return False

    def dfs(wells, bucket_cap, level, total_water):
        if not wells:
            return False
        else:
            well = wells[0]
            well_cap = grid[well[0]][well[1]]
            # print(well, well_cap, bucket_cap, level, total_water)
            if well_cap > bucket_cap:
                wells.pop(0)
                return dfs(wells, bucket_cap, level, total_water+well_cap)
            else:
                if has_space(bucket_cap - well_cap):
                    grid[well[0]][well[1]] = bucket_cap - well_cap
                    level += 1
                    return dfs(wells[1:], bucket_cap, level, total_water+well_cap)
                else:
                    return False

    for n in range(int(math.ceil(capacity)), 0, -1):
        if has_space(capacity):
            return level
        else:
            level = 0
            return dfs(wells, bucket_cap, level, 0)


