

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # Your Code Here
    max_val = l[0]
    for n in l:
        if n > max_val:
            max_val = n

    return max_val
