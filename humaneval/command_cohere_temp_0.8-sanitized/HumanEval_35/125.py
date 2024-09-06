def max_element(l: list):
    """Return maximum element in the list.

    :param l: A list of integers.
    :type l: list
    :return: The maximum element in the list.
    :rtype: int
    """
    if not l:
        raise ValueError("Cannot compute the maximum element of an empty list")
    
    # Initialize the maximum element variable
    max_el = l[0]
    
    # Traverse the list and update the maximum element, if a bigger element is found
    for num in l:
        if num > max_el:
            max_el = num
    
    return max_el