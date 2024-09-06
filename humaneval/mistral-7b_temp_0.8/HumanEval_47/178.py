

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    # Solution 1: O(nlogn)
    # a = sorted(l)
    # n = len(a)
    # if n == 1:
    #     return a[0]
    # if n % 2 == 1:
    #     return a[n//2]
    # else:
    #     return (a[n//2] + a[n//2-1])/2

    # Solution 2: O(n)
    l = sorted(l)
    n = len(l)
    m = n//2
    if n % 2 == 1:
        return l[m]
    else:
        return (l[m-1] + l[m])/2
