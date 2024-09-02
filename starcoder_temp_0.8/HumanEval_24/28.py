

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Loop through all numbers starting from 2 until n
    for i in range(2, n + 1):
        # If i divides n
        if n % i == 0:
            # Return i
            return i

    # Return None if no divisor found
    return None
