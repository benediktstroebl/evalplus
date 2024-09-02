

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    def mysort(l: list):
        if len(l) <= 1:
            return l
        else:
            pivot = l[0]
            left = [x for x in l[1:] if x < pivot]
            right = [x for x in l[1:] if x >= pivot]
            return mysort(left) + [pivot] + mysort(right)
    l = mysort(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
