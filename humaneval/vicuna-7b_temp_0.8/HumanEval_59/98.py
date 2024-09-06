

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    i = 0
    max_product = 1
    while True:
        i += 1
        if i > n / 2:
            if n % i:
                break
            else:
                product = i
                while i * i <= n:
                    if i * i % n == 0:
                        break
                    product *= i
                max_product = max(max_product, product * (i - 1) // 2)
    return max_product
