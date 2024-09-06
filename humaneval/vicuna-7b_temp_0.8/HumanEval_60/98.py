

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
    # This is an example of a recursive function.
    # It uses a helper function called sum_to_n_helper
    # to recursively calculate the sum of numbers from 1 to n.
    # The helper function takes 2 arguments: the current number
    # (n) and the current sum (total).
    # It recursively calls itself with the new sum as the current number (n)
    # and the new sum as the current total.
    # This process continues until the helper function reaches the base case
    # where the current number is 1.
    # At that point, the helper function will return the final sum.

    def sum_to_n_helper(n, total):
        if n == 1:
            return total
        return sum_to_n_helper(n-1, total + n)

    return sum_to_n_helper(n, 0)
