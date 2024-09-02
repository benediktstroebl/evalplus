

def sum_to_n(n: int):
    """sum_to_n is a function that sums numbers from 1 to n.
    >>> sum_to_n(30)
    465
    >>> sum_to_n(100)
    5050
    >>> sum_to_n(5)
    15
    >>> sum_to_n(10)
    55
    >>> sum_to_n(1)
    1
    """
    total = 0
    for i in range(1, n+1):
        total += i
    return total

pairs = [(4, 5), (2, 3), (5, 8), (1, 1), (4, 9), (3, 6), (7, 1), (7, 7), (2, 4)]
pairs.sort(key=lambda t: t[0])