
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
    # find how many times we can empty each row
    rows_empty_times = [row.count(1) for row in grid]
    # sum those
    total_empty_times = sum(rows_empty_times)
    # if total_empty_times <= bucket_capacity:
    #     return 0

    # if total_empty_times > bucket_capacity:

    # # a. find the row with the maximum number of empty times
    # max_empty_times = max(rows_empty_times)
    # max_empty_times_index = rows_empty_times.index(max_empty_times)

    # # b. find the number of times we can empty that row
    # row = grid[max_empty_times_index]
    # empty_times = row.count(1)

    # # c. if we can empty the row enough times, return 1
    # if empty_times >= bucket_capacity:
    #     return 1

    # # d. if we can empty the row fewer times, return the number of times we can empty it
    # return math.ceil(bucket_capacity / empty_times)

    # alternative:
    # TODO: modify this to run in O(1) time. 
    #  this is a slightly more complex version of the 0-1 knapsack problem

    # step 1. create a new matrix that will store the number of times we can empty each well
    #  this new matrix will have the same number of rows as the original matrix
    #  this new matrix will have one column for each number of times we can empty each well
    #  this new matrix will be as wide as the largest possible number of times we can empty a well
    #  e.g. for a 3x4 matrix, the new matrix will have a width of 4

    # step 2. loop through each row in the original matrix
    #  loop through each column in the new matrix
    #  calculate the number of times we can empty that row in that column
    #  store the number in that location in the new matrix

    # step 3. return the maximum value in the new matrix
    #  this is
