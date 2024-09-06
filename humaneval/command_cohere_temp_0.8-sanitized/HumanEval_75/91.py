def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for p in primes:
        if n % p == 0:
            return False

    c = 0
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            c += 1
    return c == 3