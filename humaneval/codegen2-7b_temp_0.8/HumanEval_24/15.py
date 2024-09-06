

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    i = 1
    largest = 0
    while n % i!= 0 and i <= n:
        if n % i > largest:
            largest = i
        i += 1
    return
