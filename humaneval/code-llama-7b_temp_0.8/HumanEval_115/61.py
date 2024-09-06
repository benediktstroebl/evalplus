
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

    def is_full(row, bucket_capacity):
        """
        Checks if given row is full.
        """
        return sum(row) >= bucket_capacity

    def get_max_row_idx(grid):
        """
        Returns the index of the row with the largest value
        """
        max_val = max(grid)
        max_row_idx = [i for i, x in enumerate(grid) if max_val in x]
        return max_row_idx[0]

    def get_row_idx(row_idx, grid):
        """
        Returns the given row
        """
        return grid[row_idx]

    def get_empty_row_idx(row_idx, grid):
        """
        Returns the index of the first empty row
        """
        return row_idx + 1 if is_full(get_row_idx(row_idx, grid), capacity) else row_idx

    def get_filled_row_idx(row_idx, grid):
        """
        Returns the index of the first filled row
        """
        return row_idx - 1 if row_idx > 0 and not is_full(get_row_idx(row_idx-1, grid), capacity) else row_idx

    def get_filled_wells(grid, bucket_capacity):
        """
        Returns a list of wells that have already been filled
        """
        filled_wells = []
        for i in range(len(grid)):
            if is_full(grid[i], bucket_capacity):
                filled_wells.append(i)
        return filled_wells

    def get_new_row_idx(row_idx, filled_wells):
        """
        Returns a new row_idx that is not in filled_wells
        """
        new_row_idx = row_idx
        while new_row_idx in filled_wells:
            new_row_idx += 1
        return new_row_idx

    def get_well_idx(row_idx, grid, bucket_capacity):
        """
        Returns the index of a
