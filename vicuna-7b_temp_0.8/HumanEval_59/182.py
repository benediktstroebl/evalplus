

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Check if n is prime
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return 2
    elif n % 3 == 0:
        return 3
    elif n % 5 == 0:
        return 5
    elif n % 7 == 0:
        return 7
    else:
        # Find the largest prime factor
        max_val = 1
        max_idx = 0
        for i in range(1, int(np.sqrt(n)) + 1):
            if n % i == 0:
                break
            if i > max_val:
                max_val = i
                max_idx = 0
        return max_val * (int(np.sqrt(n)) / max_val)
