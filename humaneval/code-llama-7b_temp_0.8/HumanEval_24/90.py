

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    largest = 1
    while largest * largest <= n:
        if n % largest == 0:
            return largest
        largest += 1

