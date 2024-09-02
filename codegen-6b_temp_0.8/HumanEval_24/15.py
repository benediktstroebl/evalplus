

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    #divisors = [d for d in range(1, n+1) if n % d == 0]
    #return divisors[-1]
    # use the binary method to find the largest divisor
    # https://stackoverflow.com/questions/41913/how-do-you-determine-the-largest-prime-factor-of-a-number
    while n % 2 == 0:
        n = n // 2
    for i in range(3, int(sqrt(n)), 2):
        while n % i == 0:
            n = n // i
    return n
