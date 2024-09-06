
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    
    num = 1

    if a == 1:
        return False

    while a > num:
        if is_prime(num) and is_prime(a/num):
            num += 1
        else:
            return False

    return True
