
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    is_prime = lambda x: all(x % i for i in range(2, x))
    if a > 100:
        return False

    for i in range(2, a//2 + 1):
        if is_prime(i) and is_prime(a // i):
            return True
    
    return False

