

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

    # We can use a while loop here to get this to work.
    # Think about how you can use the return statement to get this to work.
    result = 0
    while n > 0:
        result += n
        n -= 1
    return result

