

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    elif n % 4 == 0:
        return 4
    elif n % 5 == 0:
        return 5
    else:
        for i in range(6, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return i
        return 6