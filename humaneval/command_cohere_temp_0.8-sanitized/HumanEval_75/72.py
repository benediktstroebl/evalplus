def is_multiply_prime(a):
    # Check if a is less than 100
    if a > 100:
        return False

    # Check if a is the multiplication of 3 primes
    prime_factors = []

    while a % 2 == 0:
        prime_factors.append(2)
        a = a // 2

    # Check for all odd prime factors
    for i in range(3, int(a ** 0.5) + 1, 2):
        while a % i == 0:
            prime_factors.append(i)
            a = a // i

    if a > 1:
        prime_factors.append(a)

    return len(prime_factors) == 3
a = 30