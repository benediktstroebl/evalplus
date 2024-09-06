def is_multiply_prime(a):
    # Check if a is less than 100
    if a > 100:
        return False

    # Check if a is the multiplication of 3 primes
    factors = []
    for i in range(2, int(a ** 0.5) + 1):
        while a % i == 0:
            factors.append(i)
            a //= i
            if a == 1:
                break

    if len(factors) != 3:
        return False
    else:
        return True