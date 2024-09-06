def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    
    factors = []
    for prime in primes:
        while a % prime == 0:
            factors.append(prime)
            a //= prime
            
    return len(factors) == 3