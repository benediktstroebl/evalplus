
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
    def low_buckets(bucket, position, grid, capacity):
        '''
        buckets : array of capacity of each bucket
        position : index of the bucket currently being filled
        grid : grid of wells
        capacity : bucket capacity
        '''
        if bucket == capacity:
            return position + 1
        else:
            while position < len(grid[0]) and grid[position] == 0:
                position += 1
            if position == len(grid[0]):
                return -1
            return low_buckets(bucket + 1, position + 1, grid, capacity)

    # find all the wells
    count = 0
    for row in grid:
        # find the lowest bucket that can be filled
        wells = low_buckets(0, 0, row, capacity)
        if wells == -1:
            return -1
        count += (wells - 1)
    return count

