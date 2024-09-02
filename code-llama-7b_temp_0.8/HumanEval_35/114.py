

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # Checks if l is empty.
    if l == []:
        return None

    # Initialize largest_element to be the first element of l.
    largest_element = l[0]

    # Iterate through l[1:].
    for element in l[1:]:
        # If element is greater than largest_element, update largest_element.
        if element > largest_element:
            largest_element = element

    # Return the largest_element.
    return largest_element
