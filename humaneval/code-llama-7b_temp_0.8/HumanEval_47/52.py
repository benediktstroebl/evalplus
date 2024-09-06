

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    new_list = sorted(l)
    if len(new_list) % 2 == 0:
        median1 = new_list[len(new_list) // 2]
        median2 = new_list[len(new_list) // 2 - 1]
        return (median1 + median2) / 2.0
    else:
        return new_list[len(new_list) // 2]

