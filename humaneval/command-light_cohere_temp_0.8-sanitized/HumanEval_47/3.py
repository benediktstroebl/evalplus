def median(l: list):
    """Return median of elements in the list l"""
    if len(l) == 0:
        raise ValueError("Input list is empty")

    middle = len(l) // 2
    if len(l) % 2 == 0:
        return (l[middle][1] + l[middle][0]) / 2
    else:
        return l[middle]