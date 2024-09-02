

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # 如果列表为空或者只有一个元素
    if len(l) == 0 or len(l) == 1:
        return l[0]
    else:
        return max(l[0], max_element(l[1:]))

