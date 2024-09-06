def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = []
    
    for d in primes:
        if n % d == 0:
            divisors.append(d)
            if len(divisors) == 3:
                return True
    
    return False