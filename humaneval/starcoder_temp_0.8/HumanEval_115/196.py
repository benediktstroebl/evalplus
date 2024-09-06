
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
    # # Write your code here
    # if grid == []:
    #     return 0

    # # Number of rows
    # n = len(grid)

    # # Number of columns
    # m = len(grid[0])

    # # Number of elements in the grid
    # grid_elements = n * m

    # # Initialise the count
    # count = 0

    # # If the grid is already sorted or empty
    # # then no need to sort
    # if grid_elements == 0 or is_sorted(grid):
    #     return count

    # # Insertion sort
    # for i in range(1, grid_elements):
    #     j = i - 1

    #     # Move the current element
    #     # to the sorted part of the grid
    #     while j >= 0 and grid[j][i] > grid[j+1][i]:
    #         grid[j], grid[j+1] = grid[j+1], grid[j]
    #         j -= 1

    #     # If the current element is less
    #     # than it's previous element,
    #     # increment the count by 1
    #     if j!= i - 1:
    #         count += 1

    # # Return the count
    # return count

    if grid == []:
        return 0

    # Number of rows
    n = len(grid)

    # Number of columns
    m = len(grid[0])

    # Number of elements in the grid
    grid_elements = n * m

    # Initialise the count
    count = 0

    # If the grid is already sorted or empty
    # then no need to sort
    if grid_elements == 0 or is_sorted(grid):
        return count

    # Insertion sort
    for i in range(1, grid_elements):
        j = i - 1

        # Move the current element
        # to the sorted part of the grid
        while j >= 0 and grid[j][i] > grid[j+1][i]:
            grid[j], grid[j+1] = grid[j+1], grid[j]
            j -= 1

        # If the current element is less
        # than it's previous element,
        # increment the count by 1
        if j!= i - 1:
            count += 1

    # Return the count
    return
