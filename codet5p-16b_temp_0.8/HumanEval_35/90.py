

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """

    if l == []:
        return 0
    max_num = l[0]
    for i in range(len(l)):
        if max_num < l[i]:
            max_num = l[i]
    return max_num
