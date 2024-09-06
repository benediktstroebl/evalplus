def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Calculate each potential factor of a
        factors = [i for i in range(2, a[0] // 2 + 1) if a % i == 0]
        factors.sort()
        if len(factors) == 3:
            return all(factors)
    return False