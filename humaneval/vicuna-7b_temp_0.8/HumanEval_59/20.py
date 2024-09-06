

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Find the sqrt of n
    r = sqrt(n)
    # Find the sqrt of the sqrt of n
    k = r ** 2
    # Keep track of the largest prime we've seen
    max_prime = 2
    # Iterate through the range of 2 up to k
    for i in range(2, k):
        # Try to find a prime number
        is_prime = True
        for j in range(2, i):
            # If the number is divisible by j, it is not prime
            if not i % j:
                is_prime = False
                break
        if is_prime:
            # If this is the largest prime we've seen so far
            if max_prime < i:
                max_prime = i
    return max_prime
