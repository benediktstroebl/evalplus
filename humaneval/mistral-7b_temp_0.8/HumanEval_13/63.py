

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # BEGIN SOLUTION

    # Getting the greatest number
    greater_number = a if a > b else b
    lower_number = a if a < b else b

    # Euclidian algorithm
    while greater_number % lower_number != 0:
        greater_number, lower_number = lower_number, greater_number % lower_number

    # Returning
    return lower_number
    # END SOLUTION
