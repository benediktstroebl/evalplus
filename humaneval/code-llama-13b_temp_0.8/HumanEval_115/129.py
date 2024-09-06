
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
    nrows = len(grid)
    ncols = len(grid[0])
    # fill the bottom row with the remaining capacity
    remaining_capacity = capacity
    for j in range(ncols-1,-1,-1):
        if grid[nrows-1][j]==1:
            remaining_capacity -= 1
    # calculate the number of rounds needed to fill each column,
    # and the number of rounds needed to empty each column.
    nfill_rounds = [0]*ncols
    nexp_rounds = [0]*ncols
    for j in range(ncols):
        # fill
        for i in range(nrows-1,-1,-1):
            if grid[i][j]==1:
                remaining_capacity -= 1
                if remaining_capacity >= 0:
                    nfill_rounds[j] += 1
                else:
                    nfill_rounds[j] += math.ceil(capacity/nrows)*(-remaining_capacity//nrows)+1
                    remaining_capacity = capacity-remaining_capacity%nrows
                    break
        # empty
        remaining_capacity = capacity
        for i in range(nrows):
            if grid[i][j]==1:
                remaining_capacity -= 1
                if remaining_capacity >= 0:
                    nexp_rounds[j] += 1
                else:
                    nexp_rounds[j] += math.ceil(capacity/nrows)*(-remaining_capacity//nrows)+1
                    remaining_capacity = capacity-remaining_capacity%nrows
                    break
    # calculate the minimum number of rounds needed to empty all columns
    # by finding the maximum number of rounds needed to empty each column
    # and finding the number of rounds needed to fill the first column
    # to match the maximum round for each column.
    nmin_rounds = 0
    max_round = max(nexp_rounds)
    for j in range(ncols):
        nmin_rounds += nfill_rounds[j]-nexp_rounds[
