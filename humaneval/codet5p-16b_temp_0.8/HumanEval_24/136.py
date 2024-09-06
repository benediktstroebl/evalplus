

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    i = 1
    largest_divisor_found = 1
    while True:
        if n % i == 0:
            largest_divisor_found = i
        i += 1
        if i > n / 2:
            break
    return largest_divisor_found

