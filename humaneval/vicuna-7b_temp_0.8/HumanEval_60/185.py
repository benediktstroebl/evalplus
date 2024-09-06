

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
    # check if n is 0
    if n == 0:
        return 0
    # if n is 1, return 1
    elif n == 1:
        return 1
    # initialize sum to 0
    sum = 0
    # loop through numbers from 2 to n-1
    for i in range(2, n):
        # add i to the sum
        sum += i
    return sum

