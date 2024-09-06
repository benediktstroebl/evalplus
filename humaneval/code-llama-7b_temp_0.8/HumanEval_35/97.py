

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Note that we assume that the list is not empty
    # you may want to add an assertion that the list is not empty
    # if len(l) == 0:
    #     return None
    
    max_so_far = l[0]
    for element in l:
        if element > max_so_far:
            max_so_far = element
    return max_so_far

