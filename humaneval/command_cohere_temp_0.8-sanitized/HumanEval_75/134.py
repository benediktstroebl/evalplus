def is_multiply_prime(a):
    # Check if a is less than 100
    if a < 100:
        # Check if the prime factorization has exactly 3 factors
        return len(prime_factors(a)) == 3
    else:
        return False
def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n / 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    if n > 2:
        factors.append(int(n))
    return factors