

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
    # if n is one, just return n
    if n == 1:
        return n
    # otherwise, return the result of sum_to_n
    else:
        return n + sum_to_n(n - 1)
