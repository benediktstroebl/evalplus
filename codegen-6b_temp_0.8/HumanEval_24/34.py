

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    smaller = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i * i > n:
                return n // i
            else:
                # n is divisible by i and i * i < n, so take the largest of these
                smaller = i
    return smaller

