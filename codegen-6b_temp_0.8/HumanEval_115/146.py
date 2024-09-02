
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
    # store the wells on the grid
    n, wells = len(grid), [None] * len(grid)
    for i in range(n):
        wells[i] = set(range(len(grid[0])))
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                wells[i].remove(j)

    # travese the wells line by line and use BFS to traverse to the empty cells
    count, rows, cols = 0, len(wells), len(wells[0])
    # hash the empty wells as a lookup table
    well_to_neighbor = {well : set() for well in wells}
    for i in range(len(wells)):
        for j in wells[i]:
            well_to_neighbor[(i, j)].add((i, j - 1))
            well_to_neighbor[(i, j)].add((i, j + 1))
            well_to_neighbor[(i, j)].add((i - 1, j))
            well_to_neighbor[(i, j)].add((i + 1, j))

    # use BFS to traverse and fill all the wells
    for well in wells:
        if not well:
            # well = [0,0]
            # well[0] = 0
            # well[1] = 0
            # well_to_neighbor[well] = set([well])
            # neighbors = set([well])
            # queue = [well]
            # while queue:
            #     neighbor = queue.pop(0)
            #     for loc in well_to_neighbor[neighbor]:
            #         if loc not in wells:
            #             wells[loc] = capacity
            #             wells[well] += 1
            #             count += 1
            #         else:
            #             neighbors.add(loc)
            #     queue.extend(neighbors)

            # start from the first well, and fill all the wells
            queue, neighbors = [well], set([well])
            while queue:
                