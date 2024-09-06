def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = []
    
    for prime in primes:
        if n % prime == 0:
            divisors.append(prime)
    
    return len(divisors) == 3