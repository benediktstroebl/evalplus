

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    # Approach 1
    # return max(l)

    # Approach 2
    # m = l[0]
    # for x in l:
    #     if x > m:
    #         m = x
    # return m

    # Approach 3
    # m = None
    # for x in l:
    #     if m is None or x > m:
    #         m = x
    # return m

    # Approach 4
    m = None
    for x in l:
        if m is None:
            m = x
        else:
            if x > m:
                m = x
    return m

