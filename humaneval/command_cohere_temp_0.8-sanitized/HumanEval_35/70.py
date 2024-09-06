def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
        l (list): List of elements.
    
    Returns:
        int or float: Maximum element in the list.
    """
    if not l:
        raise ValueError("List cannot be empty")
    
    max_el = l[0]
    for num in l:
        if num > max_el:
            max_el = num
    return max_el