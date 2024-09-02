
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
    def extra_water(grid, capacity):
        """
            Minimum extra water required to be collected from all wells to make all wells watered.
        """
        extra_water = 0
        for row in grid:
            # filter all 1s
            units = list(filter(lambda x: x == 1, row))
            # if all are 1, return 0
            if len(units) == len(row):
                continue
            # if not, calculate the extra water required
            extra_water += capacity - sum(units)
        return extra_water

    def max_water_trap(grid):
        """
            Maximum water you can trap between the walls of each well.
        """
        max_water = 0
        for row in grid:
            left, right = 0, len(row) - 1
            left_max, right_max = 0, 0
            while left < right:
                if row[left] < row[right]:
                    if row[left] > left_max:
                        left_max = row[left]
                    else:
                        max_water += left_max - row[left]
                    left += 1
                else:
                    if row[right] > right_max:
                        right_max = row[right]
                    else:
                        max_water += right_max - row[right]
                    right -= 1
        return max_water

    def max_fill(grid, capacity):
        """
            Maximum water you can get from all wells.
        """
        extra_water = extra_water(grid, capacity)
        return max(max_water_trap(grid) + extra_water, 0)

    return max_fill(grid, capacity)
