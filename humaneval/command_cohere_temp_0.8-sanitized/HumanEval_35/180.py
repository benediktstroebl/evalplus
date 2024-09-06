def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list of elements.

    Returns:
        int or float: The maximum element in the list.
    """
    # Initialize the maximum element to the first element of the list
    max_el = l[0] if l else None

    # Iterate through the list and update the maximum element if a larger value is encountered
    for el in l:
        if el > max_el:
            max_el = el

    return max_el