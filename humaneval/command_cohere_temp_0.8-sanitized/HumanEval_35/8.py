def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list of elements.

    Returns:
        int or float: The maximum element in the list.
    """
    if not l:
        raise ValueError("The input list is empty. Cannot determine the maximum element.")

    max_element = max(l)
    return max_element