

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    coprime_list = [int(i) for i in range(1, n)]
    for i in coprime_list:
        if n % i == 0:
            coprime_list.remove(i)
    return max(coprime_list)

