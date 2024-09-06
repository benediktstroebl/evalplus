def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Make a list of the prime factors of n
    pf = []
    while n % 2 == 0:
        pf.append(2)
        n = n / 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            pf.append(i)
            n = n / i
    if n > 2:
        pf.append(n)
    # Return the largest element of the list
    return max(pf)