
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 1:
        return False
    i = 2
    n = 3
    while n ** 2 <= a:
        if a % n == 0:
            return False
        n += 1
    return True
        
