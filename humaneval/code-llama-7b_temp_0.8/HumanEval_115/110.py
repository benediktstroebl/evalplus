
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

    def process_grid(grid, capacity):
        """
        Process the grid.
        """
        import math

        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    grid[i][j] = math.inf
                else:
                    grid[i][j] = 0

        return grid

    def process_grid_reverse(grid, capacity):
        """
        Process the grid.
        """
        rows, cols = len(grid), len(grid[0])
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if grid[i][j] > 0:
                    grid[i][j] = math.inf
                else:
                    grid[i][j] = 0

        return grid

    def find_lowest_well(grid, capacity):
        """
        Find the lowest well.
        """
        rows, cols = len(grid), len(grid[0])

        lowest_well = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    lowest_well.append((i,j))

        if len(lowest_well) == 0:
            return []
        return lowest_well

    def get_top_right(grid, i, j, capacity):
        """
        Get the top right coordinate of the well.
        """
        rows, cols = len(grid), len(grid[0])

        top_right = []
        if i > 0:
            top_right.append((i-1, j))
        if j < cols-1:
            top_right.append((i, j+1))

        return top_right

    def get_top_left(grid, i, j, capacity):
        """
        Get the top left coordinate of the well.
        """
        rows, cols = len(grid), len(grid
