
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
    # Find the leftmost well and find all the open cells
    # Start with the leftmost well and loop through the rest of the wells
    # Check for cells that are open but not filled up and fill it up. 
    # Increment counter if the current counter is greater than the capacity of the bucket
    # Recursively run the function for the remaining wells
    # return the counter
    # O(n^3) time | O(n) space
    if not grid:
        return 0
    # Find the leftmost well
    leftmost_well_index = get_leftmost_well(grid)
    leftmost_well = grid[leftmost_well_index]
    # get open cells from the leftmost well
    open_cells = get_open_cells(leftmost_well)

    def helper(grid, bucket_capacity, current_well_index, current_counter):
        if not grid:
            return current_counter
        if current_well_index == len(grid):
            return current_counter
        current_well = grid[current_well_index]
        filled_cells = [cell for cell in current_well if cell!= 0]
        if len(filled_cells) == len(current_well):
            return helper(grid, bucket_capacity, current_well_index + 1, current_counter)
        bucket_capacity -= len(filled_cells)
        if bucket_capacity > 0:
            return helper(grid, bucket_capacity, current_well_index + 1, current_counter)
        else:
            current_counter += 1
            current_well = [0] * len(current_well)
            for cell in filled_cells:
                current_well[cell] = 1
            return helper(grid, bucket_capacity + len(filled_cells), current_well_index + 1, current_counter)

    return helper(grid, capacity, leftmost_well_index + 1, 0)

