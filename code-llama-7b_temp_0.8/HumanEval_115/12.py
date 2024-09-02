
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
    def find_min_max(grid):
        """
        Find the maximum and minimum water that can be stored
        in a well and return them.
        """
        import math
        left_max, right_max = 0, 0
        for row in grid:
            left, right = 0, len(row) - 1
            while left <= right:
                if row[left] == 1:
                    left_max = max(left_max, left)
                    break
                left += 1
            while left <= right:
                if row[right] == 1:
                    right_max = max(right_max, right)
                    break
                right -= 1
        return min(left_max, right_max), max(left_max, right_max)
    
    def fill_water(grid, left_max, right_max, capacity):
        """
        Fill the water in each well.
        """
        import math
        min_max, max_max = find_min_max(grid)
        water_used = 0
        for row in grid:
            left, right = 0, len(row) - 1
            while left <= right:
                if row[left] == 1:
                    right_min, left_min = min_max, max_max
                    while left <= left_min and row[left] == 1:
                        left_min = left - 1
                    while right >= right_min and row[right] == 1:
                        right_min = right + 1
                    water_used += min(capacity, math.ceil((right_min - left_min - 1) / 2))
                    left += 1
                elif row[left] == 0:
                    left += 1
                right -= 1
        return water_used
    
    left_max, right_max = find_min_max(grid)
    return fill_water(grid, left_max, right_max, capacity)
