
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
    def fill_well(row, col):
        """
        Recursive function to fill a well.
        It calculates the current amount of water in a well and 
        if it can be completely filled, it calls itself recursively on the next well.
        The recursion stops when the well has been completely filled.
        """
        if col >= len(grid[row]): return
        if not grid[row][col]: return
        # Get the number of water units in the well
        amount = 0
        for x in range(col, len(grid[row])):
            if not grid[row][x]: break
            amount += 1
        # Calculate the number of times we can fill the bucket and the remaining water units
        times = math.ceil(amount / capacity)
        remaining = amount % capacity
        # Fill the well
        for x in range(col, col + times * capacity):
            grid[row][x] = 0
        # Recursively call fill_well on the next well
        fill_well(row, col + times * capacity + 1)

    # Main loop that calls fill_well on each well
    times = 0
    for row in range(len(grid)):
        fill_well(row, 0)
        times += 1
    return times
