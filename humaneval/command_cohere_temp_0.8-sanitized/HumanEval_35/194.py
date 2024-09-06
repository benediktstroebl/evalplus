def max_element(l: list):
    """Return maximum element in the list.

    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if not l:
        return None  # Return None if the list is empty

    max_el = l[0]  # Initialize the maximum element with the first element of the list

    for el in l:
        if el > max_el:  # Compare each list element to the current maximum
            max_el = el  # Update the maximum element if a larger element is found

    return max_el