
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
    # we have a grid of wells with each well having the same length
    # each bucket has a capacity
    # for each well, find the number of times we need to lower the bucket
    # to empty the well
    # what is the maximum number of times we need to lower the bucket to empty the well
    # we can start at any well and go across the wells by going down each row of the grid
    # we can only empty the well if the capacity of the bucket is greater than the value of the well
    # we can move to the next well if we've used up all of the available capacity in the current bucket
    # we can lower the bucket by using 1 unit of the well value or we can lower the bucket by using all of the available capacity
    # it is not possible to use more than the available capacity
    # we can calculate this by dividing the available capacity by the well value
    # in this way we can count the number of times we need to lower the bucket to empty the well
    # the more we move across the wells, the more times we need to lower the bucket
    # this is because the capacity of the bucket is going to be used more the more we move across the wells
    # the amount that we need to lower the bucket by is the lesser of the available capacity or the well value
    # we can find the number of times we need to lower the bucket by taking the minimum between the number of times we need to lower the bucket by using 1 unit of the well value and the number of times we need to lower the bucket by using all of the available capacity
    # since we only need to take the minimum, we can calculate the minimum by dividing the available capacity by the well value
    # therefore, our algorithm will be O(r * c) where r is the number of rows and c is the number of columns
    # we can find the maximum number of times we need to lower the bucket by taking the maximum between the minimum number of times we need to lower the bucket by using 1 unit of the well value and the number of times we need to lower the bucket by using all of the available capacity
    # since we only need to take the maximum, we can calculate the maximum by dividing the available capacity by the maximum possible value of the wells
    # therefore, our algorithm will be O(r * c) where r is the number of rows and c is the number of columns
    # space
