

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
    # Use a helper function to avoid having to use recursion in the main function
    def helper(n, a, b):
        if n == 0:
            return a
        else:
            return helper(n-1, a + (n//b)*(b-1), b)

    # Call the helper function with n=1
    a = helper(1, 1, n)
    # Start with the initial value of the sum
    return a
