

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    if n % 2 == 0:
        divisor = 2
        while n % divisor!= 0:
            divisor += 1
    else:
        divisor = 3
        while n % divisor!= 0:
            divisor += 2
    return divisor

