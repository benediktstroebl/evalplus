def is_multiply_prime(a):
    # Write a function that returns true if the given number is the multiplication of 3 prime numbers
    # and false otherwise
    limit = int(sqrt(a)) + 1
    for i in range(2, limit):
        if a % i == 0:
            return False
    
    for i in range(2, limit):
        if a % i == 0 and is_prime(i):
            return False
    
    return True
def is_prime(n):
    # Return true if the number is a prime, false otherwise
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True