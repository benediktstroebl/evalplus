
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
    # create a set to store the unique digits
    unique_digits_set = set()
    # iterate through the list
    for num in x:
        # check if the number has any even digit
        if num % 2 == 0:
            continue
        # add the digit to the set
        unique_digits_set.add(num)
    # return the sorted list of unique digits
    return [str(num) for num in unique_digits_set]