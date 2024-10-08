
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    while a > 0:
        if a % 3 == 0 and is_prime(a // 3):
            a = a // 3
            continue
        if a % 5 == 0 and is_prime(a // 5):
            a = a // 5
            continue
        return False
    return True

