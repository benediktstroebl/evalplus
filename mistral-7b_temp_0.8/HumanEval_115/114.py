
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
    n_rows, n_cols = len(grid), len(grid[0])
    # create the queue of indexes of the wells to fill
    q = [(i, j) for i in range(n_rows) for j in range(n_cols) if grid[i][j] == 1]
    # create the set of indexes already filled
    filled = set()
    # create the set of positions to fill
    filled_positions = set()
    # create the bucket and initialize it with the given capacity
    bucket = set([capacity])
    # keep going until all the wells are filled
    while q and filled < filled_positions:
        # calculate the distance to the next empty well
        distance = int(math.sqrt(sum(map(pow, q[0], 2))))
        # add the current position to the filled set
        filled.add(q.pop(0))
        # add the distance to the filled set of positions
        filled_positions.add(distance)
        # update the bucket with the new capacity
        bucket = set(filter(lambda x: x
