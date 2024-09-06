

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
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    sum = 0
    for n_1 in range(1, n + 1):
        sum += n_1

    return sum