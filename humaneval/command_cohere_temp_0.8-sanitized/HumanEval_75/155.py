def is_multiply_prime(a):
    # check if a is less than 100
    if a > 100:
        return False
    
    # check if a is the multiplication of 3 primes
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    for prime in prime_numbers:
        if a % prime == 0:
            return True
    
    return False