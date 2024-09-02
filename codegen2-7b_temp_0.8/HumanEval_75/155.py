
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    i=0
    while i < len(a):
        if not is_prime(a[i]) or not is_prime(a[i+1]) or not is_prime(a[i+2]):
            return False
        i += 3
    
