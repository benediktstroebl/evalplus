
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
    # use a for loop to iterate through the list
    #if the number is not even, append to list
    #if it is even, check for divisibility by 4, if so, append to list
    #if it is not divisible by 4, append to list
    #return list
