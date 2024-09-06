

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Traverse through the list
    for i in l:
        # Check if element is smaller than current max element
        if i > max:
            # If it is, update current max element
            max = i
    return max
