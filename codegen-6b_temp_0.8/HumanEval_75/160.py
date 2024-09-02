
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 100:
        a = [i for i in range(2, a) if i % 2 != 0 and i % 3 != 0 and i % 5 != 0]
        return True if len(a) == 0 else False
    return False

