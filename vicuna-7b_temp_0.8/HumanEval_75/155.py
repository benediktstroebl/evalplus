
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    n = int(a)
    if n < 1:
        return False
    while n <= 99:
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False
        n = n + 2
    return True
