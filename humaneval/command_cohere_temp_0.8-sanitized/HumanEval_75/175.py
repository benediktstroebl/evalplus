def is_multiply_prime(a):
    # Check if a is less than 100
    if a > 100:
        return False

    # Check if a is the product of 3 primes
    prime_numbers = [2, 3, 5, 7, 11, 13]
    factors = []
    
    for prime in prime_numbers:
        while a % prime == 0:
            factors.append(prime)
            a //= prime
            
    if a > 1 or len(factors) != 3:
        return False
    
    factors.sort()
    return factors[0] * factors[1] * factors[2] == a