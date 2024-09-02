
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
    #helper function to get the location of a cell in the grid
    def get_index(grid, i, j):
        return grid[i][j]

    #helper function to set the location of a cell in the grid
    def set_index(grid, i, j, val):
        grid[i][j] = val

    #helper function to get the location of a cell in the grid
    def get_location(grid, i):
        return grid[i]

    #helper function to set the location of a cell in the grid
    def set_location(grid, i, val):
        grid[i] = val

    #helper to check if a point is inside a grid
    def point_inside_grid(grid, pt):
        return 0 <= pt[1] < len(grid[0]) and 0 <= pt[0] < len(grid)

    #helper to check if a cell is inside a bucket
    def cell_is_inside_bucket(grid, i, j, capacity):
        if i == 0:
            return True
        elif j == 0:
            return True
        elif get_index(grid, i-1, j) == 1:
            return capacity >= get_index(grid, i, j)
        elif get_index(grid, i-1, j-1) == 1:
            return capacity + get_index(grid, i, j) >= get_index(grid, i, j-1)
        else:
            return False

    #helper to update the index of a cell inside a bucket
    def update_index(grid, i, j, capacity, val):
        if cell_is_inside_bucket(grid, i, j, capacity):
            set_index(grid, i, j, val)

    #helper to remove a cell inside a bucket
    def remove_cell(grid, i, j):
        set_index(grid, i, j, 0)

    #helper to get the capacities of all buckets
    def get_bucket_capacities(grid):
        return [get_index(grid, i, -1) for i in range(len(grid))]

    #hel