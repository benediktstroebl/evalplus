def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    - l (list): List of elements
    
    Returns:
    - int or float: Maximum element in the list
    
    Example:
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # check if the list is empty
    if not l:
        return None
    # initialization
    max_so_far = l[0]
    for x in l:
        # update max_so_far if a number is greater than the current max
        if x > max_so_far:
            max_so_far = x
    return max_so_far