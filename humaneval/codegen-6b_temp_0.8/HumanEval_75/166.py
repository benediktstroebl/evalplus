
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a > 100:
        return False
    sqrt_num = a ** 0.5
    for i in range(int(sqrt_num)):
        if not prime(i) and not prime(a - i):
            return False
    return True

