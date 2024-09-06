

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # base case
    if n < 3:
        return 2

    # we know that n >= 3, so the next step is to check if n is prime.
    # if n is prime, we are done.
    if n % 2 == 0:
        return 2

    # if n is odd, it is prime.
    if not n % 3:
        return 3

    # if n is odd, and n % 2 != 0, then it is odd and composite.
    # so we know the largest prime factor is n-1.
    # the next largest prime factor is n-2.
    # we keep dividing by 2 until we find the smallest prime factor.
    # this is done by repeatedly taking the floor of n/2.
    # after the floor of n/2 is taken, n becomes n-1, and we continue
    # this process until n=2.
    # this approach is called Euclid's algorithm and it will always
    # find the gcd of two numbers.
    while True:
        if n % 2 == 0:
            floor_n = int(n / 2)
            n = n - floor_n
        else:
            floor_n = int(n / 2) + 1
            n = n - floor_n
        if n == 1:
            return floor_n
        if n % 2 == 0:
            break

    # at this point, we have found the smallest prime factor of n.
    # the largest prime factor is n - 1.
    return n - 1
