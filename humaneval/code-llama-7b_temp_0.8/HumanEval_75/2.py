
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        x = 0
        i = 1
        while i <= a:
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                x += 1
            if x == 3:
                return True
            i += 1
        return False
    return False
    
