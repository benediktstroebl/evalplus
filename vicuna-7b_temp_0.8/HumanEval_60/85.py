

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
    # the sum of numbers from 1 to n
    result = 0
    # loop over the numbers from 1 to n
    for i in range(1, n+1):
        result += i
    return result
