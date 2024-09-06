
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    #  We can iterate the values from 3 to the given number,
    #  since we want to know if the number is a multiple of 3.
    for i in range(3, a):
        if a % i == 0:
            # If it is a multiple of any number, it must not be a multipul of 3
            return False
    return True

