
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
    # WRITE YOUR CODE HERE
    # first we will calculate the minimum number of steps needed
    # we will use bfs

    num_of_steps = 0

    # we will use the dist dictionary to store the number of steps needed to
    # get from each cell to the source cell (0, 0)
    # the dist dictionary is used as a cache
    dist = {}
    dist[(0, 0)] = 0

    # we will use a queue to traverse the grid
    queue = []
    queue.append((0, 0))

    # we will keep traversing the grid until we find the source cell
    while queue:
        # we will get the cell that we will visit next
        row, col = queue.pop(0)

        # we will get the number of steps needed to get to that cell
        steps = dist[(row, col)]

        # we will get the cells adjacent to the current cell
        # we will check each cell if it is not out of bounds and not visited
        # and if the value at the cell is 1 (the cell
