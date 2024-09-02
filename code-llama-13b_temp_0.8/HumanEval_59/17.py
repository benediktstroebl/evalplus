

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # divide by 2 until it is no longer even
    # then start at 3 and increment by 2 and check to see if the number is a multiple of it
    if n % 2 == 0:
        return largest_prime_factor(n//2)
    for i in range(3, int(n**0.5), 2):
        if n % i == 0:
            return max(i, largest_prime_factor(n//i))
    return n

