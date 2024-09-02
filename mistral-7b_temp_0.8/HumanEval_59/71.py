

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Your code goes here
    result = 0
    for number in range(2, n):
        if n % number == 0:
            if is_prime(number):
                result = number
        if n % number == 0 and is_prime(number):
            result = number
    return result
