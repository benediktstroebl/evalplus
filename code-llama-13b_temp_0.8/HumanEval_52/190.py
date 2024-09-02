

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    # 如果l的长度是0，则返回False
    if len(l) == 0:
        return False
    # 如果l的长度是1，则返回l中的第一个数是否小于t
    if len(l) == 1:
        return l[0] < t
    # 如果l的长度是2，则返回l中的两个数是否都小于t
    if len(l) == 2:
        return l[0] < t and l[1] < t
    # 如果l的长度大于等于3，则返回l中所有的数都小于t
    return l[0] < t and l[1] < t and l[2] < t and below_threshold(l[3:], t)
