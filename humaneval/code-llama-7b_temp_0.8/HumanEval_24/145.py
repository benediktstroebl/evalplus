

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # largest divisor cannot be greater than n / 2
    largest_divisor = int(n / 2)
    # check for divisibility of n / i
    for i in range(largest_divisor, 1, -1):
        if n % i == 0:
            largest_divisor = i
            break
    return largest_divisor

