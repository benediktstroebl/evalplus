
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

    def fill_well(well, capacity, left_bottle, right_bottle):
        if left_bottle == right_bottle:
            return 0
        if well[left_bottle] == 1:
            return fill_well(well, capacity, left_bottle, (left_bottle+right_bottle)//2)
        if well[right_bottle] == 1:
            return fill_well(well, capacity, (left_bottle+right_bottle)//2, right_bottle)
        if well[left_bottle] == 0 and well[right_bottle] == 0:
            if capacity > 1:
                return max(fill_well(well, capacity-1, left_bottle, (left_bottle+right_bottle)//2), 
                fill_well(well, capacity-1, (left_bottle+right_bottle)//2, right_bottle))
            return math.inf
    
    def fill_grid(grid, capacity):
        return fill_well(grid, capacity, 0, len(grid))

