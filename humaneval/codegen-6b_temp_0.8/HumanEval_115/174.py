
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
    def find_bucket(row, col):
        """
        Find the bucket given the row, col coordinates
        """
        return row * (col+1) + col

    def find_well(row, col):
        """
        Find the well given the row, col coordinates
        """
        return (row+1) * (col+1) - row - col - 1

    def lower_bucket(row, col, bucket_height):
        """
        Lower the bucket at the given row, col
        """
        well = find_well(row, col)
        well_col = well % col
        well_row = (well - well_col) / col
        cur_row = row
        cur_col = col
        delta = 1
        while cur_row != well_row:
            well = find_well(cur_row, well_col)
            well_bucket = find_bucket(well_row, well_col)
            if delta > bucket_height:
                well = find_well(cur_row, cur_col)
                well_bucket = find_bucket(cur_row, cur_col)
                delta = well_bucket - well
            else:
                well_bucket = well + delta
            well = find_well(cur_row, cur_col)
            well_bucket = find_bucket(cur_row, cur_col)
            cur_row = well_row
            well = well + delta
            well_bucket = well_bucket + delta
            grid[well_bucket][well_col] += 1
            grid[well_row][well_col] -= 1
            well = find_well(cur_row, cur_col)
            well_bucket = find_bucket(cur_row, cur_col)
            cur_col = well_col
            delta = well_bucket - well

    def host_empty(row, col, bucket_height):
        """
        Empty the well given the row, col coordinates
        """
        well = find_well(row, col)
        well_col = well % col
        well_row = (well - well_col) / col