

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:
        return True
    m_d = None
    if l[0] <= l[1]:
        m_d = '+'
    else:
        m_d = '-'
    for i in range(1, len(l) - 1):
        if m_d == '+':
            if l[i] >= l[i+1]:
                return False
        else:
            if l[i] <= l[i+1]:
                return False
    return True

