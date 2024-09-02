

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # We start from the number itself, and work our way down
    divisor = n

    # We can use a while loop as long as divisor is greater than 1
    while divisor >= 2:

        # We can use the modulo (%) operator, which gives the remainder of a division
        # We expect the remainder to be 0 if the number divides evenly
        if n % divisor == 0:
            return divisor

        # We can decrease the divisor by 1
        divisor -= 1

    # We should never reach here because n should always have a factor larger than 1
    # But to be safe, we return -1 if that is the case
    return -1

