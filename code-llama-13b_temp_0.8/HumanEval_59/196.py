

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest = None
    end = int(n**0.5) + 1
    for i in range(2, end):
        if n % i == 0:
            if largest is None or largest < i:
                largest = i
    return largest

