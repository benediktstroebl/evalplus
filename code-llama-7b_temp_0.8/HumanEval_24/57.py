

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # return max([i for i in range(1, n) if n % i == 0])
    largest = 1
    # Check if n is evenly divisible by 2
    if n % 2 == 0:
        largest = 2

    i = 3
    while i * i <= n:
        if n % i == 0:
            largest = i
        i = i + 2
    return largest

