
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
    if a % 2 == 0 or a % 3 == 0:
        return False
    sqr = int(a ** 0.5)
    for i in range(5, sqr + 1, 6):
        if a % i == 0 or a % (i + 2) == 0:
            return False
    return True
