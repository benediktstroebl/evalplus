

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # check if list is empty
    if l == []:
        raise ValueError("List is empty.")
    # sort the list in ascending order
    l.sort()
    if len(l) % 2 == 0:
        # if list length is even
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        # else list length is odd
        return l[len(l) // 2]

