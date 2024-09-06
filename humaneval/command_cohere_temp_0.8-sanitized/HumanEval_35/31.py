def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
        l (list): List of elements.
    
    Returns:
        int or float: Maximum element in the list.
    """
    if not l:
        raise ValueError("List cannot be empty")
    
    max_element = max(l)
    return max_element