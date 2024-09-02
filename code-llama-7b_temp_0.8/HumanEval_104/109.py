
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

    # make a copy of the input list to prevent mutation
    x = list(x)

    # get rid of elements with any even digit
    for i in range(len(x)):
        # flag for removing element
        remove = False

        # convert to string for checking
        x_str = str(x[i])

        # check every digit of the number
        for j in range(len(x_str)):
            digit = int(x_str[j])

            # remove if even digit
            if digit % 2 == 0:
                remove = True
                break

        # remove number if even digit found
        if remove == True:
            x.remove(x[i])

    # return sorted list
    return sorted(x)

