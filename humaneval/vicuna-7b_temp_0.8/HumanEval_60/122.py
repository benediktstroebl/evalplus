

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
    # Check if n is a valid number
    if n < 1 or n > 99:
        raise ValueError

    # Initialize the sum
    sum = 0

    # Loop through the numbers from 1 to n
    for i in range(1, n+1):
        # Add the current number to the sum
        sum += i

    # Return the sum
    return sum
