def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for prime in primes:
        if n % prime == 0:
            return False

    divisors = [i for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
    for div in divisors:
        for prime in primes:
            if div == prime:
                continue
            if div == n / prime:
                return False

    return True