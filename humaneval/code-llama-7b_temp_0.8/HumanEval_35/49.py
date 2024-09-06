

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Maximum element in the list
    max_elem = l[0]
    # Loop from index 1 till the last index of the list
    for i in range(1, len(l)):
        # If the maximum element is less than the current element
        if max_elem < l[i]:
            # Assign the current element as the maximum element
            max_elem = l[i]
    return max_elem

