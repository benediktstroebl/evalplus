

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    # 以 Python 的 built-in 函数 nth_element 实现，并且更加简洁和高效
    return max(l[0], (l[1],) + l[2:])