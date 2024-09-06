
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if(a <= 0):
        return False
    if(a == 1):
        return False
    i = 0
    while i <= 10:
        if((a%(i + 1)) == 0):
            if(is_prime(i + 1)):
                i += 1
            else:
                return False
        else:
            return False
        i += 1
    return True
