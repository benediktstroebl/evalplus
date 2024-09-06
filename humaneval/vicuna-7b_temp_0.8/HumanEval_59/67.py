

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(n: int, ps: list):
        for i in range(1, n):
            if n % i == 0:
                return False
        return True

    def get_smallest_p(n: int, ps: list):
        p = n
        while p > 1 and is_prime(p, ps):
            p = p - 2
        return p

    def get_largest_p(n: int, ps: list):
        p = n
        while p > 1 and is_prime(p, ps):
            p = p + 2
        return p

    def largest_prime_factor_helper(n, ps, largest_p):
        if n == 1:
            return largest_p
        if n in ps:
            return largest_prime_factor_helper(get_smallest_p(n, ps), ps, largest_p)
        if n % 2 == 0:
            return largest_prime_factor_helper(2, ps, largest_p)
        if n > 2:
            p = get_largest_p(n, ps)
            if largest_p < p:
                largest_p = p
        return largest_p

    largest_p = largest_prime_factor_helper(n, list(range(2, int(n**0.5) + 1)), 2)
    return largest_p
