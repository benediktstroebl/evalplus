def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    - l (list): List of elements
    
    Returns:
    - max (int or str): Maximum value in the list
    """
    max_ = max(l, key=lambda x: x)
    return max_