

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # start by dividing by 2 if it is divisible.
    while n % 2 == 0:
        n = n // 2
    i = 3
    largest_prime = 1
    # loop through the odd numbers.
    while i * i <= n:
        if n % i == 0:
            largest_prime = i
            n = n // i
        else:
            i = i + 2
    # if n is greater than 2.
    if n > 2:
        largest_prime = n
    return largest_prime

