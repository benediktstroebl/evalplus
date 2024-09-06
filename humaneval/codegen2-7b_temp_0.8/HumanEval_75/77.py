
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if (a < 100):
        return False
    n = a
    while n % 3 == 0:
        n = n / 3
    while n % 5 == 0:
        n = n / 5
    return n == 1
