
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 10:
        return False
    if a % 2 != 0:
        return False
    p = 1000000
    while p < a:
        p = (p + 6768) % a
        if (p - 2 * (p % a) + a) % a == 0:
            return False
    return True