
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
    def get_fill_required(grid, capacity):
        width = len(grid[0])
        height = len(grid)
        # we can start from top left
        # and keep adding the water till we reach the height of the water
        # we can fill at most the capacity of bucket
        # hence we add the capacity to the grid at each position till we reach the height
        # of the water
        # we also have to keep in mind that we need to fill the well till all the water is filled
        # so we have to take the min of all the values in the grid
        if grid[0][0] == 1:
            return 0
        grid = [[grid[0][0] + (capacity * (i + 1)) for i in range(width)] for j in range(height)]
        grid = [[math.min(grid[i][j], grid[i][j + 1]) if j < width - 1 else grid[i][j] for j in range(width)] for i in range(height)]
        grid = [[math.min(grid[i][j], grid[i +
