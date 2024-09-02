
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    
    # YOUR CODE HERE
    
    # Note:
    # you can assume that the result will be an integer
    
    # take x
    x_int = int(x)
    
    # take y
    y_int = int(y)
    
    # check if x is bigger
    if x_int > y_int:
        # x is bigger
        # find the highest number in the range
        highest_num = x_int
    else:
        # y is bigger
        # find the highest number in the range
        highest_num = y_int
    
    # check if x number is even
    if x_int%2 == 0:
        # is even
        # check if x is in the range
        if x <= highest_num:
            # is in the range
            # find the highest number in the range
            highest_num = highest_num - 2
    
    # check if y number is even
    if y_int%2 == 0:
        # is even
        # check if y is in the range
        if y_int >= highest_num:
            # y is in the range
            # find the highest number in the range
            highest_num = highest_num - 2
    
    # check if the result is negative
    if highest_num < 0:
        return -1
    
    # return the result
    return highest_num

