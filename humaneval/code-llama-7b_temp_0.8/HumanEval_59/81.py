

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    max_prime = 2
    for i in range(2, n + 1):
        if i * i > n:
            break
        elif n % i == 0:
            n //= i
            max_prime = i
    if n > max_prime:
        max_prime = n
    return max_prime

