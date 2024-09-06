
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
    if a == 2:
        return True
    if a % 3 == 0:
        return False
    for x in range(4, int(a ** 0.5) + 1, 2):
        if a % x == 0:
            return False
    return True
