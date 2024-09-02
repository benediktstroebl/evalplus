

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Set the initial maximum to the first element
    maximum = l[0]
    # Loop through the list
    for i in l:
        # if an element is greater than the current maximum, set the maximum to be that element
        if i > maximum:
            maximum = i
    return maximum
