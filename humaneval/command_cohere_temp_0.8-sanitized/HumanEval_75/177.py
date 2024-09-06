def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = set(range(2, int(a**0.5) + 1)) | {a}
    for prime in primes:
        if prime not in divisors:
            return False
    return len(divisors) == 3