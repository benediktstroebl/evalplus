
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a % 2 == 0:
        return False
    if a % 3 == 0:
        return False
    if a < 100:
        return True
    k = 5
    while k * k <= a:
        if a % k == 0:
            return False
        if a % (k + 2) == 0:
            return False
        k += 6
    return True

