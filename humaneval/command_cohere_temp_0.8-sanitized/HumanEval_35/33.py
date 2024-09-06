def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list.

    Returns:
        int or float: The maximum element in the list.
    """

    # Initialize maximum value
    max_value = float('-inf')

    # Iterate through the list and update the maximum value
    for element in l:
        if element > max_value:
            max_value = element

    return max_value