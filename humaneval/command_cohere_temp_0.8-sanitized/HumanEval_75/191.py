def is_multiply_prime(n):
    primes = [2, 3, 5]
    while len(primes) < 3:
        next_primes = [p * p for p in primes if p != 1]
        primes.extend(next_primes)
    return n == primes[0] * primes[1] * primes[2]