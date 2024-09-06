
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
    print(f"max_fill grid: {grid}")
    # find the max length of the grid
    max_well = 0
    for row in grid:
        if len(row) > max_well:
            max_well = len(row)
    print(f"max_well: {max_well}")

    # count the number of 1s in each row
    well_1s = []
    for row in grid:
        well_1s.append(row.count(1))
    print(f"well_1s: {well_1s}")

    # determine the number of full wells
    # a full well is a well that has more 1s than the capacity
    num_full = 0
    for num_1 in well_1s:
        if num_1 > capacity:
            num_full += 1
    print(f"num_full: {num_full}")

    # remove the full wells
    new_grid = []
    for i in range(len(grid)):
        if grid[i].count(1) > capacity:
            pass
        else:
            new_grid.append(grid[i])
    print(f"new_grid: {new_grid}")

    # find the longest contiguous 1s
    longest = 0
    for i in range(len(new_grid)):
        row = new_grid[i]
        for j in range(len(row) - longest):
            num_1 = 0
            for k in range(j, j + capacity):
                if k >= len(row):
                    break
                if row[k] == 1:
                    num_1 += 1
            if num_1 == capacity:
                longest = j + capacity

    print(f"longest: {longest}")

    # count the number of times we need to lower the bucket
    # round up the fill up
    total_fill = round(longest / capacity)
    print(f"total_fill: {total_fill}")

    # add the number of times we have to lower the bucket
    return total_fill + num_full
