
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if a is prime
    if not is_prime(a):
        return False
    
    # Check if a is 3
    if a == 3:
        return True
    
    # Check if a is a product of 2 prime numbers
    if is_prime(a-1) and is_prime(a+1):
        return True
    
    # Check if a is a product of 3 prime numbers
    for p in range(a-1, a+2):
        if is_prime(p) and is_prime(p+2) and is_prime(p+4):
            return True
    
    return False
