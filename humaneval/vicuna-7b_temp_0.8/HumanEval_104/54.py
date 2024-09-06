
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
    # sort the list
    x.sort()
    # initialize variables to track if the number contains even digit
    even_found = 0
    # initialize variables to store the unique digits
    unique_digits = []
    # iterate through each element in the list
    for i in x:
        # if the number doesn't contain any even digit
        if not (i % 2 == 0):
            # append the number to the unique_digits list
            unique_digits.append(i)
            # increment the even_found variable
            even_found += 1
    # check if there are any odd digit left
    while even_found % 2 != 0:
        unique_digits.append(x[-1])
        even_found += 1
    # return the sorted unique digits list
    return unique_digits
