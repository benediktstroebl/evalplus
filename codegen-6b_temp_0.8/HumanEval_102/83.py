
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # Check if x is an integer and y is an integer
    if type(x) != int or type(y) != int:
        return -1

    # Initialize the first value to -1
    max_num = -1

    # Check if x is not greater than y
    if x <= y:
        return -1

    # Check if x is odd
    if x % 2 != 0:
        # Get the upper limit of x / 2
        upper_limit = int((x+1)/2)
        # Check for each value in the range from 1 to upper limit
        for i in range(1, upper_limit):
            # Check if the value is even and is greater than the max num
            if (i%2 == 0) and (i > max_num):
                # Set the max_num to i
                max_num = i
    else:
        # If x is even, get the lower limit of x / 2
        lower_limit = int((x/2))
        # Check for each value in the range from 1 to upper limit
        for i in range(1, lower_limit):
            # Check if the value is even and is greater than the max num
            if (i%2 == 0) and (i > max_num):
                # Set the max_num to i
                max_num = i
    
    # Return the max num if it is greater than 0
    return max_num
