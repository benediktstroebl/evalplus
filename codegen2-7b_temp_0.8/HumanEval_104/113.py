
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
    
    def digit_gen(x):
        if x == 0:
            return x
        elif x % 2 == 0:
            return digit_gen(x//10)
        else:
            return x
        
    return sorted(x, key=digit_gen)
    
