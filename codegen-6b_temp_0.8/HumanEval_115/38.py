
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
    def is_well(row):
        num_wells = sum(row)
        return num_wells == capacity
  
    def is_well_a(row):
        # Returns True if all the wells in a row are well, and False otherwise
        row_wells = [well for well in row if well == 1]
        return len(row_wells) == len(row)
  
    def is_well_b(row):
        # Returns True if all the wells in a row are well, and False otherwise
        # Two consecutive wells -> (well1 || NOT equal to well2)
        for i in range(len(row) - 1):
            well_a, well_b = row[i], row[i+1]
            if well_a != well_b:
                return False
        return True
  
    def fill_wells(row):
        # Returns the number of wells filled in a row
        num_wells = sum(row)
        return num_wells - capacity

    # Find the first row where we have well after the previous row
    # We are reducing the number of times we are lowering the buckets.
    def step_one(row):
        for i in range(1, len(row)):
            next_well = row[i]
            prev_well = row[i-1]
            if next_well and not prev_well:
                return i
        return len(row)

    # We are now at the first row where we have well after the last row.
    # Decrease the number of times we are lowering the buckets.
    def step_two(row):
        last_well = row[-1]
        if last_well:
            return len(row)
        else:
            return step_one(row[:-1]) - 1

    # We are now at the first row where we have well after the last row.
    # Decrease the number of times we are lowering the buckets.
    def step_three(row):
        last_well = row[-1]
        if last_well:
            return len(row)
        else:
            return step_one(row[:-1]) - 1

    def step