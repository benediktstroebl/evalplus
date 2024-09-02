
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    # initializing an empty list to hold the required result
    res = []
    # looping over each element in the list
    for num in x:
        # converting each number to string for further processing
        str_num = str(num)
        # initializing a flag to store the condition of the loop
        flag = True
        # looping over each digit in the string
        for i in str_num:
            # if any digit is even, mark the flag as False
            if int(i) % 2 == 0:
                flag = False
                break
        # if the flag is True, append the number to the result list
        if flag:
            res.append(num)
    # sort the result list in ascending order
    res.sort()
    # return the result list
    return res

