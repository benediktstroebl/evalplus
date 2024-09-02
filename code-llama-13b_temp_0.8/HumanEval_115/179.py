
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
    
    #==============================================================
    # Preprocess the grid
    #==============================================================
    
    # Find the length of each row in the grid
    row_len = len(grid[0])
    
    # Find the number of rows in the grid
    num_rows = len(grid)
    
    # Find the number of wells in the grid
    num_wells = num_rows * row_len
    
    #==============================================================
    # Construct a simple object to access the wells
    #==============================================================
    
    # Define the well object to abstract away the grid indices
    class Well(object):
        def __init__(self, grid, row_idx, col_idx, row_len):
            self.grid = grid
            self.row_idx = row_idx
            self.col_idx = col_idx
            self.row_len = row_len
        
        @property
        def water(self):
            return self.grid[self.row_idx][self.col_idx]
        
        @property
        def right(self):
            return self.water and self.col_idx + 1 < self.row_len
        
        @property
        def left(self):
            return self.water and self.col_idx > 0
        
        @property
        def below(self):
            return self.water and self.row_idx + 1 < num_rows
        
        @property
        def above(self):
            return self.water and self.row_idx > 0

        @property
        def left_neighbor(self):
            return Well(self.grid, self.row_idx, self.col_idx - 1, self.row_len)
        
        @property
        def right_neighbor(self):
            return Well(self.grid, self.row_idx, self.col_idx + 1, self.row_len)
        
        @property
        def above_neighbor(self):
            return Well(self.grid, self.row_idx - 1, self.col_idx, self.row_
