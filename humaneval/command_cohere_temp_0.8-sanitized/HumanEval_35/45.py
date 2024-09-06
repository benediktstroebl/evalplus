def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # initialize maximum element
    max_so_far = float('-inf')

    # traverse the list and update max_so_far if a number is greater than max_so_far
    for num in l:
        if num > max_so_far:
            max_so_far = num

    return max_so_far