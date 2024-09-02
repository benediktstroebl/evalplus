
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
    # your code goes here
    row, column = len(grid), len(grid[0])
    # find the number of columns that can be filled by a single bucket
    # the bucket can hold water from max. 2 columns
    bucket_size = 2 * capacity + 1

    # convert the grid to a binary string
    binary_string = ""
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                binary_string += "1"
            else:
                binary_string += "0"

    # find the length of the binary string
    binary_length = len(binary_string)

    # convert the binary string to a decimal number
    decimal_number = int(binary_string, 2)

    # find the number of digits in the decimal number
    digits = len(str(decimal_number))

    # convert the number of digits to an array of digits
    digits = list(str(decimal_number))
    # print(digits)

