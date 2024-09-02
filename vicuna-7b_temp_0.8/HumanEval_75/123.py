
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
    for x in range(2, n):
        if n % x == 0:
            return False
    for y in range(2, n-1):
        if n % y == 0:
            return False
    for z in range(n-1, 0, -1):
        if n % z == 0:
            return False
    return True