

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    """
    for number in l:
        if number >= t:
            return False
    return True
    """
    # 用列表推导式
    return not any(number >= t for number in l)

