

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

    # make sure n is a positive integer
    assert n >= 1 and int(n) == n, "n must be a positive integer"

    # make sure n is an integer
    try:
        n = int(n)
    except:
        return "n must be a positive integer"

    # return the sum
    return sum(range(1, n+1))

