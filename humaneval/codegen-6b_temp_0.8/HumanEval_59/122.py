

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # My initial idea
    # gcd = math.gcd(n, 2)
    # if gcd == 1:
    #     return 2
    # else:
    #     if n % gcd == 0:
    #         return gcd
    #     else:
    #         return largest_prime_factor(n / gcd)
    # My improved version
    
    # while n % 2 == 0:
    #     n = n / 2
    #     gcd = math.gcd(n, 2)
    #     if gcd == 1:
    #         return 2
    # return n if gcd == 1 else largest_prime_factor(n / gcd)
    
    # My better version
    # n_sqrt = int(math.sqrt(n))
    # for i in range(2, n_sqrt + 1):
    #     gcd = math.gcd(i, n)
    #     if gcd == 1:
    #         return i
    # return n

    # My best version
    while n % 2 == 0:
        n /= 2
    return 2 if n == 1 else largest_prime_factor(n)
