
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 3:
        return False
    if a == 2:
        return True
    if a == 3:
        return True
    if a % 2 == 0:
        return False
    if a % 3 == 0:
        return False
    if a % 5 == 0:
        return False
    if a % 7 == 0:
        return False
    for i in range(9, int(a**(1/2)) + 1, 2):
        if a % i == 0:
            return False
    for i in range(11, int(a**(1/3)) + 1, 2):
        if a % i == 0:
            return False
    for i in range(13, int(a**(1/5)) + 1, 2):
        if a % i == 0:
            return False
    return True
