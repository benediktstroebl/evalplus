
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for i in range(2, 100):
        if factor_one(i, 3):
            if factor_two(i, 3):
                if factor_three(i, 3):
                    return True
    return False

