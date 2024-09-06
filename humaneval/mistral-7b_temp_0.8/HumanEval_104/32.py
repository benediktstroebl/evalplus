
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
    #if the list contains only 0 or 1 numbers, then return an empty list
    if len(x) <= 1:
        return []
    #create a list that contains the unique numbers from the list x
    y = [str(i) for i in x]
    #sort the list y in increasing order
    y.sort()
    #create a new list called z that contains the numbers from y
    #only if all the digits of that number are odd
    z = [i for i in y if not '0' in str(i)]
    #sort the list z in increasing order
    z.sort()
    return z

