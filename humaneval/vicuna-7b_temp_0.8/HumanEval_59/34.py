

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # 2**31 = 2048
    if n == 2048:
        return 2
    # check if n is a prime
    if not is_prime(n):
        # find the largest prime factor of n
        for d in div_fact(n):
            if is_prime(d):
                return d
        # if n is not prime and we've tried all divisors, return the first prime we found
        return max(div_fact(n), key=lambda x: is_prime(x))
    else:
        # recursively find the largest prime factor
        return max(largest_prime_factor(n // i) for i in range(2, int(log(n, 2)) + 1))
