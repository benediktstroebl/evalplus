

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
        # find all the factors of n
        factor_list = []
        for i in range(1, n + 1):
            if n % i == 0:
                factor_list.append(i)
        # factor_list = list(filter(lambda x: n % x == 0, range(1, n + 1)))

        # find the largest prime factor
        largest_factor = 1
        for factor in factor_list:
            is_prime = True
            for i in range(2, factor):
                if factor % i == 0:
                    is_prime = False
            if is_prime and factor > largest_factor:
                largest_factor = factor

        return largest_factor

