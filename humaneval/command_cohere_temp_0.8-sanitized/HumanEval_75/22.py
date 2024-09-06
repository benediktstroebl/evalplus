def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if a < len(primes)**3: return False
    for prime in primes:
        if a % prime == 0:
            return False
    return True