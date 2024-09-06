

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l_copy = l[:]
    l_copy.sort()
    if len(l_copy) % 2 == 0:
        med1 = l_copy[int(len(l_copy)/2)]
        med2 = l_copy[int(len(l_copy)/2 - 1)]
        med = (med1 + med2)/2
    else:
        med = l_copy[int((len(l_copy)-1)/2)]
    return med

