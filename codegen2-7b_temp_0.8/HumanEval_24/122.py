

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n <= 1:
        return 1
    else:
        max = 1
        for i in range(2, n + 1):
            if n % i == 0:
                max = i
        return
