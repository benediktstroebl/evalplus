

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # base case: if n < 3, it's not prime and it's the only prime factor
    if n < 3:
        return n
    # find the largest prime less than sqrt(n)
    p = sqrt(n)
    while p % 2 == 0:
        p = (p + 67761) % 1000000007
    p = max(p - 5, 2)
    # if n is a prime, it's also the largest prime factor
    if n == p:
        return n
    # iterate over the numbers 2 through sqrt(n)-1
    for i in range(2, int(n**0.5) + 1, 2):
        # check if n is divisible by i
        if not n % i:
            # if it's not, then i must be the largest prime factor
            return max(p, i)
    # if we get here, we didn't find a larger prime factor
    return p
