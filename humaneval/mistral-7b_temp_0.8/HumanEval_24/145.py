

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Let's assume that the largest divisor is 1
    largest_divisor = 1
    # Let's assume that the divisor we're checking is 2
    divisor = 2
    # Let's assume that the result of a division of n by divisor is whole
    n_div_by_divisor = n // divisor
    # As long as the divisor is less than the largest divisor, we increase the divisor and check if the result of the division is whole
    while divisor < largest_divisor:
        divisor += 1
        n_div_by_divisor = n // divisor
    # If the result of the division is whole, we increase the largest_divisor to the divisor
    if n_div_by_divisor == 1:
        largest_divisor = divisor
    # Otherwise, we return the largest divisor
    return largest_divisor

