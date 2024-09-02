
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
    #@param grid: a 2D array
    #@param capacity: an integer
    #@return an integer
    """
    This problem was asked by Google.

    You are given a rectangular grid of wells, where each well has an x, y coordinate, and a capacity.
    Here, capacity is measured by the number of water units that you can pump out of the well.
    For example, if the well at x = 2, y = 5 had a capacity of 2 units, you could pump out 2 units of water from that well.

    Write an algorithm that computes, in one sweep of the grid, the total volume of water (both in wells and pumped out), 
    and the total volume of water pumped out of wells into other wells. 
    (Don't forget about the bucket's capacity!)

    Assume that you can lift up and put down the bucket in wells directly.
    """
    rows = len(grid)
    cols = len(grid[0])
    water = sum(sum(grid,[]))
    water_pumped_out = 0

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] != 0:
                #get the capacity of this well
                w = min(grid[x][y], capacity)

                #pump out the water from the current well
                water_pumped_out += w

                #remove the water from this well
                grid[x][y] -= w

                #fill up the current well
                grid[x][y] = capacity

                #add water from the bucket to the current well and the wells above and to the left
                for x_iter in range(x, -1, -1):
                    for y_iter in range(y, -1, -1):
                        if grid[x_iter][y_iter] < capacity:
                            grid[x_iter][y_iter] += 1

    #print("water {}".format(water))
    #print("water pumped out {}".format(water_pumped_out))
    return int(
