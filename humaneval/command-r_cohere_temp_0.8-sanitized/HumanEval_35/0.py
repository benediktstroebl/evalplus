def max_element(l: list):
    """Return the maximum element in the list.
    Args:
        l (list): A list of integers.

    Returns:
        int: Maximum element in the list.
    """
    max_val = float('-inf')
    for num in l:
        if num > max_val:
            max_val = num
    return max_val