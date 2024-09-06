
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
    
    if x == []:
        return []
    
    even_digits = [int(i) for i in str(x[0]) if int(i) % 2 == 0]
    odd_digits = [int(i) for i in str(x[0]) if int(i) % 2!= 0]
    
    return sorted(odd_digits + unique_digits(even_digits) if len(even_digits) > 0 else odd_digits
