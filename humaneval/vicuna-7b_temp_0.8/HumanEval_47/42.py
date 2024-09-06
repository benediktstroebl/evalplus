

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    n = len(l)
    if n % 2 == 0:
        m = (n // 2) - 1
        return sum(l[m*i:(m+1)*i] for i in range(1, n // 2 + 1)) / 2
    else:
        if n % 3 == 0:
            return sum(l[i*3:(i+1)*3] for i in range(1, n // 3 + 1)) // 3
        else:
            return l[n//2]
