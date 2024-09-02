
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
    
    def flatten(matrix):
        return [j for i in matrix for j in i]
    
    def h(barrel):
        return math.ceil(barrel / capacity)

    def v(well):
        return 0 if well == 0 else well

    def hv(well, barrel):
        return h(barrel) + v(well)

    def next_row(row, capacity, grid):
        return row + 1 if capacity > sum(flatten(grid[row])) else row

    def remove_row(row, capacity, grid):
        for well in range(len(grid[row])):
            grid[row][well] = 0
        return row - 1

    def remove_row_all(row, capacity, grid):
        return remove_row(row, capacity, grid) if capacity > sum(flatten(grid[row + 1])) else row - 1

    def remove_rows(grid, capacity, prev_wells, to_remove):
        new_wells = [prev_wells[well] for well in to_remove]
        if capacity > sum(flatten(grid[prev_wells[-1]])):
            return new_wells
        return remove_row_all(prev_wells[-1], capacity, grid)

    def remove_rows_all(grid, capacity, prev_wells, to_remove):
        return remove_rows(grid, capacity, prev_wells, to_remove) if capacity > sum(flatten(grid[prev_wells[-1]+1])) else prev_wells[:-1]

    wells = len([well for row in grid for well in row if well])
    wells_to_remove = [well for row in grid for well in row if well == 0]
    wells_to_remove = remove_rows_all(grid, capacities[0], [0] * wells, wells_to_remove)

    wells_to_remove = remove_rows_all(grid, capacities[0], wells_to_remove, [wells] * wells)

    return wells_to_remove
