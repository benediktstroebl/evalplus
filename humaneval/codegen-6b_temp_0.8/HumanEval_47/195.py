

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    lst = sorted(l)
    if len(lst) % 2 == 0:
        lst1 = lst[:len(lst)//2]
        lst2 = lst[len(lst)//2:]
        return float(sum(lst1) + sum(lst2)) / (len(lst1) + len(lst2))
    else:
        return lst[len(lst)//2]

