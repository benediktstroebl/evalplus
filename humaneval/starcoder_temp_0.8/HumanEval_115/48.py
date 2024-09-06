
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
    # Get max water that can be stored in each row
    max_water = [max(x) for x in grid]

    # Get height of each row
    height = [0] * len(grid)
    for i in range(len(height)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                height[i] += 1

    # Get row index of each cell
    row_index = [0] * len(grid)
    for i in range(len(height)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                row_index[j] = i

    # Iterate over each cell
    count = 0
    for j in range(len(grid[0])):
        # Check if we can store water
        if grid[row_index[j]][j] == 1:
            # Get water capacity of current row
            cap = capacity - height[row_index[j]]
            # Find the minimum amount of water to store in this cell
            min_water = min(cap, max_water[row_index[j]])
            # Calculate how many rows need to be lowered
            count += math.ceil(min_water / capacity)
            # Subtract water from the row
            max_water[row_index[j]] -= min_water
            # Update the height of the row
            height[row_index[j]] += min_water

    return count
