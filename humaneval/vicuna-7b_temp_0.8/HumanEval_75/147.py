
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 10:
        return True
    if a % 2 == 0:
        return False
    if a == 3:
        return True
    if (a - 2) % 2 == 0:
        return False
    if a == 5:
        return True
    for x in range(6, int(a**0.5)+1, 2):
        if (a - x**2) % x == 0:
            return False
    return True
