def is_multiply_prime(a):
    prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = []
    
    for prime in prime_list:
        if a % prime == 0:
            divisors.append(prime)
    
    return len(divisors) == 3