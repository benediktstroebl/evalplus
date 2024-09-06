def is_multiply_prime(a):
    # check if a is 1, in that case multiplication with any number will be 1 and this will not be prime
    if a == 1:
        return False
    
    # check if a is divisible by 2, in that case it is not prime
    if a % 2 == 0:
        return False
    
    # check divisibility by odd numbers (3, 5, 7, ...)
    for i in range(3, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return False
    
    return True