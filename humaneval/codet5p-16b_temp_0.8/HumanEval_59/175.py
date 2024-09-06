

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    if n == 1:
        return 1
    else:
        list_of_factors = []
        prime_factors = []
        for i in range(2, n):
            if n % i == 0:
                list_of_factors.append(i)
        for i in list_of_factors:
            if (largest_prime_factor(i)) == i:
                prime_factors.append(i)
        if len(prime_factors) == 0:
            return n
        else:
            return max(prime_factors)
