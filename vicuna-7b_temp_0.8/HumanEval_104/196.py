
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
    #sort the list
    x.sort()
    #get the indices of odd numbers
    odd_indices = [i for i, n in enumerate(x) if n % 2 != 0]
    #get the values of the elements in the odd indices
    odd_values = [n for i, n in enumerate(x) if i in odd_indices]
    #get the sorted list of the odd values
    sorted_odd_values = sorted(odd_values)
    #return the sorted list of the odd values
    return sorted_odd_values
