

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
    # Initialize an empty list to store the sum of numbers from 1 to n
    # Multiply the length of the list by 1 to get the sum of 1 to n
    # Divide the result by 2 to get the sum of 1 to n/2
    # Divide the sum of 1 to n/2 by 2 to get the sum of 1 to n/4
    # Repeat the process until the length of the list is 1
    # Return the last element of the list
    return [x + x for x in range(1, n + 1) / 2] / 2
