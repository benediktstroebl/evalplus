

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # The largest divisor must also be smaller than n
    result = n - 1

    # We need to test all numbers from 2 to n
    for i in range(2, n):
        if n % i == 0:
            # This is a divisor
            result = i

    return result
