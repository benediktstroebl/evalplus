
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

    if not grid:
        return 0
    if not grid[0]:
        return 0
    if len(grid) == 1:
        return 0

    if sum(grid[0]) == 0:
        return 0
    if sum(grid[0]) < capacity:
        return len(grid[0])

    rows = len(grid)
    cols = len(grid[0])

    def extract_water(i, j, capacity):
        """
        Extract water from the wells using buckets.
        If it is possible to extract water from the wells, return the number of buckets used to extract water.
        If it is not possible to extract water from the wells, return -1.
        """
        #print(f'extract water {i}, {j}, {capacity}')
        if not grid[i][j]:
            return -1

        # extract water from the well
        grid[i][j] = 0
        #print(f'extract water {i}, {j}, {capacity}')

        # extract water from the row below
        if i+1 < rows:
            #print(f'extract water {i}, {j}, {capacity}')
            res = extract_water(i+1, j, capacity-1)
            if res != -1:
                #print(f'extract water {i}, {j}, {capacity}')
                return res + 1

        # extract water from the column to the right
        if j+1 < cols:
            #print(f'extract water {i}, {j}, {capacity}')
            res = extract_water(i, j+1, capacity-1)
            if res != -1:
                #print(f'extract water {i}, {j}, {capacity}')
                return res + 1

        return -1

    def fill_water(i, j, capacity):
        """
        Fill water into the wells using buckets.
        If it is possible to fill water into the wells, return the number of buckets used to fill water.
        If it is not possible to fill water into the wells
