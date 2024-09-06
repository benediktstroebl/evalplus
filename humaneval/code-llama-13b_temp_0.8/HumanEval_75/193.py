
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        num = 2
        while num < a:
            if a % num == 0:
                if a / num == num:
                    return True
                else:
                    return False
            num += 1
        return True
    return False

