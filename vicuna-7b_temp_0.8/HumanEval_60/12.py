

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
    # Write a recursive implementation of sum_to_n
    # using a helper function that takes an integer n and
    # returns the sum of 1 and the nth number.
    def helper(n):
        if n == 1:
            return 1
        else:
            return n + helper(n-1)
    
    result = helper(n)
    return result
