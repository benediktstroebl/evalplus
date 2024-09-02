

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
    # This implementation uses recursion to sum numbers from 1 to n
    # We pass the current sum to the next call of the function
    # The first call has a sum of 1, and the next calls have a sum of 1 plus the previous sum
    # This continues until the sum is equal to n
    if n == 0:
        return 0
    return n + sum(sum_to_n(i) for i in range(1, n + 1))
