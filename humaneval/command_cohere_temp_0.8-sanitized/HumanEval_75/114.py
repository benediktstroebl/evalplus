def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Count the unique divisors of the number a
        div = set(int(i) for i in range(1, int(a ** 0.5) + 1) if a % i == 0)
        if len(div) == 3:
            return True
    return False