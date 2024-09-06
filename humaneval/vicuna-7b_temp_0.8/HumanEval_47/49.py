

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n % 2 == 0:
        return (n//2) + 1.0
    else:
        k = int((n + 1) // 2)
        left = [x for x in l[0:k-1] if x < median(l[k:])]
        right = [x for x in l[k:][::-1] if x >= median(l[k:])]
        return sum(left) + sum(right)
