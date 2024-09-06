

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    largest_divisor = 1
    for divisor in range(2, n + 1):
        if n % divisor == 0:
            if divisor > largest_divisor:
                largest_divisor = divisor
            break
    return largest_divisor

