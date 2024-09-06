
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        return a % 2 == 0
    
    # Boringly simple
    for i in [2, 3, 5]:
        a = a / i
        if a < 100:
            return a % 2 == 0
        elif a < 1000:
            return False
    
    return True

