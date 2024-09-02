

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 0:
        raise ValueError("n must be positive")

    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        for i in range(2, n+1):
            if n % i == 0:
                return i
    # return 1 if n is a prime number
    # return n if n is a prime number
