
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check if the number is prime
    if not is_prime(a):
        return False
    
    # Check if the square of the number is prime
    if not is_prime(a**2):
        return False
    
    # Check if the cube of the number is prime
    if not is_prime(a**3):
        return False
    
    # Check if the number is a prime number
    if a > 100:
        return True
    return False
