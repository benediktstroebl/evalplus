
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    flag = False
    if a < 30:
        return False
    for i in range(2, a / 3):
        if a % i == 0:
            flag = True
    return not flag

