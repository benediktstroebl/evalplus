
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
    # #Initial Thoughts : 
    #    1. This problem can be reduced to filling the well to the middle by
    #    2. if the grid is of even dimensions then start from the middle and fill it to the edges
    #    3. if the grid is of odd dimension then start from the top-middle and bottom-middle and fill it to top-left and top-right respectively
    #    4. when the two of these are full then fill the next row to the top-middle and bottom-middle
    
    #    1. the key here is to fill the entire rows one by one
    #    2. first, check if the grid is odd or even
    #    3. then, fill the left row or rows with equal amount of water to the bucket capacity
    #    4. then, fill the right row or rows with equal amount of water to the bucket capacity
    #    5. continue this process until the grid is filled
    
    #    1. the time complexity is O(n^2) because of the nested loops
    #    2. the space complexity is O(1) because we are using constant storage
    
    #    1. let's start with the base case
    #    2. then, we need to check if the grid is of odd dimensions
    #    3. if it is, then we need to start filling it from the top-middle to the bottom
    #    4. else we need to start filling from the left-middle to the right-middle
    
    #    1. let's get the dimensions of the grid
    #    2. let's declare the total times to be filled
    #    3. let's declare the number of times to fill the left and the right rows
    #    4. let's declare the bucket capacity
    #    5. let's declare the left and right rows
    #    6. let's declare the number of rows and columns
    #    7. let's check if the grid is of odd dimensions
    #    8. let's initialize the left row or rows with equal amount of water to the bucket capacity
    #    9. let's initialize the right row or rows with equal amount of water to the bucket capacity
    #    10. let's iterate until
