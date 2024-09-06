

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
    return (n ** 2 / 2) + (n ** 3 / 6) + (n ** 4 / 24) + (n ** 5 / 24) + (n ** 6 / 24) + (n ** 7 / 24)
