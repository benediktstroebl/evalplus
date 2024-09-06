

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Initialize a variable to store the largest prime factor
    largest_prime = n

    # Loop through each possible divisor, from 2 to n
    for divisor in range(2, n+1):
        # if n is divisible by divisor
        if (n % divisor) == 0:
            # if divisor is prime
            if is_prime(divisor):
                # update the largest prime factor
                largest_prime = divisor

    # return the largest prime factor
    return largest_prime

