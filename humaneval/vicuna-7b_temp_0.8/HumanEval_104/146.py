
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
    # sort the input list
    x.sort()

    # initialize a set to keep track of the unique digits
    unique_digits = set()

    # loop through the sorted list
    for i in x:
        # get the digits of the current number
        digits = str(i)

        # remove any even digits from the digits
        digits = ''.join([d if d % 2 != 0 else d for d in digits])

        # add the digits to the set of unique digits
        unique_digits.add(digits)

    return sorted(unique_digits)