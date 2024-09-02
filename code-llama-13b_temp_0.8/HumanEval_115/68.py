
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
    # create buckets list of buckets to contain collected water
    buckets = [0] * capacity
    # iterate through the grid
    for row in grid:
        # set two pointers, one at the head of the row, the other at the tail of the row
        left = 0
        right = len(row) - 1
        # while both pointers do not collide
        while left < right:
            # if the left pointer's water is greater than capacity
            if row[left] > capacity:
                # if the right pointer's water is less than capacity
                if row[right] <= capacity:
                    # move the left pointer to the right
                    left += 1
                # otherwise
                else:
                    # move the right pointer to the left
                    right -= 1
            # otherwise
            else:
                # if the right pointer's water is less than capacity
                if row[right] <= capacity:
                    # move the right pointer to the left
                    right -= 1
                # otherwise
                else:
                    # move the left pointer to the right
                    left += 1
        # sum the bucket water in the row
        for i in range(len(row)):
            buckets[min(i, capacity - 1)] += row[i]
    # sum the total water collected in the grid
    water_collected = sum(buckets)
    # return the number of times the buckets are filled
    return math.ceil(water_collected / capacity)
