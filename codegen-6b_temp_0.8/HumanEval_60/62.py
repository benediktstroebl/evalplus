

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
    # numbers = range(1, n + 1)
    # sum = 0
    # for number in numbers:
    #     sum += number
    # return sum
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)

from math import sqrt