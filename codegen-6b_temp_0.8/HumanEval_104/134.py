
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
    unique_nums = []
    for num in x:
        digits = str(num)
        has_even = False
        for c in digits:
            if int(c)%2 != 0:
                has_even = True
                break
        if not has_even:
            unique_nums.append(num)
    return sorted(unique_nums)
        


        
        
        
        
    



