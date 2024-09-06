def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in primes:
        if n % prime == 0:
            return False

    divisors = [divisor for divisor in range(1, int(n ** 0.5) + 1) if n % divisor == 0]
    return len(divisors) == 3