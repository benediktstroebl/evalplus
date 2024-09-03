def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 is not a prime"""
    if not is_prime(n):
        return 0
    # Find the largest prime factor
    largest = 0
    for i in range(2, int(n**0.5) + 1):
        if is_prime(i):
            largest = i
            break
    return largest