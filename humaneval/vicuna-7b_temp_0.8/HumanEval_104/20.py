
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
    # sort the input list in ascending order
    x.sort()
    # create a set to store the digits that have been seen
    digits = set()
    # iterate through the sorted list
    for i in range(len(x)):
        # check if the current digit is even
        if x[i] % 2 == 0:
            # if it is even, add the digit and its position to the set
            digits.add(x[i])
            digits.add(i+1)
        else:
            # if it is odd, add the digit to the set
            digits.add(x[i])
    # remove the digits that have been seen from the set
    digits = list(digits)
    # return the sorted list of unique digits
    return sorted(digits)
