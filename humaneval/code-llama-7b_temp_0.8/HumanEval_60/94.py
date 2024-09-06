

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
    # Set the sum equal to 0.
    sum = 0
    # Loop over numbers 1 to n.
    for i in range(1, n+1):
        # Add the number to the sum.
        sum = sum + i
    # Return the sum.
    return sum

