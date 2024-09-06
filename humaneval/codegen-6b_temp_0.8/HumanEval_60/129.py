

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
    "*** YOUR CODE HERE ***"
    sum1 = 0
    sum2 = 0
    for i in range(1, n + 1):
        if not i % 3:
            sum1 += i
        if not i % 5:
            sum2 += i
    return sum1 + sum2
