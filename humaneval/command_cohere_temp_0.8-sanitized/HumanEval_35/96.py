def max_element(l: list):
    """Return maximum element in the list.

    Args:
        l (list): The input list of elements.

    Returns:
        int or float: The maximum element in the list.
    """
    # Initialize the maximum element to the first element of the list
    max_element_ = l[0]
    # Iterate over the list and update the maximum element if a larger element is encountered
    for num in l:
        if num > max_element_:
            max_element_ = num
    # Return the maximum element
    return max_element_