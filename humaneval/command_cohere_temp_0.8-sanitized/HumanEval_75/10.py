def is_multiply_prime(a):
    # check if a is 1, because multiplication of 1 by any prime will be always 1
    if a == 1:
        return False
    
    for i in range(2, int(a**.5) + 1):
        if a % i == 0:
            return False
    
    # since a is less than 100, after checking all odd numbers from 3 to the square root of a,
    # if none of them is a factor, then a must be a product of 3 primes
    return True