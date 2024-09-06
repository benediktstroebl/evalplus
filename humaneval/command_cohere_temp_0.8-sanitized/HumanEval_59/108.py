def largest_prime_factor(n):
    """Return the largest prime factor of n."""
    # Write n as 2^a * 3^b * 5^c * ... * p_k^l
    # Where a, b, c ... , l are maxues 0, 1, ... , k-1
    # respectively
    # So we take the max of each exponent
    exp = 0
    max_power = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
            exp += 1
        elif n % 3 == 0:
            n //= 3
            exp += 1
        elif n % 5 == 0:
            n //= 5
            exp += 1
        else:
            max_power = exp
            # Found a prime factor, so return n
            return n
        if n == 1:
            break
    return max(n, n ** max_power)