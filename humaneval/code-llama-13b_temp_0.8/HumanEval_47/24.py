

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    new_list = l[:]
    new_list.sort()

    if len(new_list) % 2 == 0:
        index = int(len(new_list) / 2)
        return (new_list[index - 1] + new_list[index]) / 2
    else:
        return new_list[int(len(new_list) / 2)]

