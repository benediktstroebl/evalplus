

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest = 1
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            if n / i > largest:
                largest = n / i
    return largest
