def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    # Your code here. Make sure to use only Python concepts and functionalities!

    # You can assume that n is not 1, since that would be a special case and the function would return 1, a valid answer. However, it is not advised to handle such special cases in an algorithmically oriented challenge like this.
    assert n > 1 and not is_prime(n), "Unexpected input. Ensure n is greater than 1 and composite."

    # Iterative approach utilizing Python's built-in features
    largest_factor = n
    for potential_factor in range(2, int(n ** 0.5) + 1):
        if n % potential_factor == 0:
            largest_factor = potential_factor
        elif is_prime(potential_factor):
            return potential_factor

    return largest_factor
def is_prime(n):
    """Check if n is prime."""
    if n < 2:
        return False
    for potential_divisor in range(2, int(n ** 0.5) + 1):
        if n % potential_divisor == 0:
            return False
    return True