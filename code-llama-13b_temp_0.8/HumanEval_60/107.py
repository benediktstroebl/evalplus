

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
    # start our sum at 0
    sum = 0
    # iterate through all the values
    for i in range(1, n + 1):
        # add each value to the sum
        sum += i
    # return the sum
    return sum

