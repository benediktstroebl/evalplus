def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return not any(factor in factors for prime in primes for factor in primes if prime ** 3 > factors[factor] or n % prime == 0)