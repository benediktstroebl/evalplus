

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # It's important to understand how this solution works. 
    # Try to reason through it before you try to decode it.

    # IMPORTANT: Don't worry if you don't completely understand
    # the solution right away. Give it a little time.

    # This solution starts by looking at the first and last elements
    # in the list and comparing them. If the first element is bigger
    # than the last element, the first element is returned.
    #
    # Otherwise, if the first element is not bigger than the last element,
    # then the solution looks at the second and last elements.
    # If the second element is bigger than the last element,
    # then the second element is returned.
    # Otherwise, if the second element is not bigger than the last element,
    # then the solution looks at the third and last elements, and so on.
    #
    # This process continues until it reaches the end of the list,
    # or the element it is looking at is bigger than the current maximum.
    # In this case, the element it was looking at will be the maximum.
    #
    # Notice that at no point is the maximum element itself
    # compared to itself.

    if len(l) == 0:
        raise ValueError('Cannot get the maximum of an empty list')

    max = l[0]

    for i in range(1, len(l)):
        if l[i] > max:
            max = l[i]

    return max

