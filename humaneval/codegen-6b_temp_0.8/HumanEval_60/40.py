

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
    def helper(n):
        """helper is a nested function that sums numbers from 1 to n."""
        sum = 0
        if n > 1:
            sum = helper(n - 1)
        return sum + n
    return helper(n)

