def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Check for the largest possible factor numerically
    largest_factor = n // 2
    while True:
        if n % 2 == 0:
            n //= 2
        else:
            break
    # Iterate through possible divisors 2 times the largest factor
    for i in range(3, largest_factor * 2 + 1, 2):
        while n % i == 0:
            n //= i
            if i == largest_factor:
                return i
            elif i > largest_factor:
                largest_factor = i
    if n > 1:
        return n