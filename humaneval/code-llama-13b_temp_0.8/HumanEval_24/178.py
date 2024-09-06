

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    if n % 2:
        return largest_divisor(n-1)
    half = n // 2
    if half * half == n:
        return half
    for i in range(3, half+1, 2):
        if n % i == 0:
            return i
    return 1

