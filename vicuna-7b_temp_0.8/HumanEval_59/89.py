

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    max_factor = 2
    max_remainder = 1
    for num in range(3, int(n**0.5) + 1, 2):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            max_factor = num
            max_remainder = n // num
    return max_factor, max_remainder
