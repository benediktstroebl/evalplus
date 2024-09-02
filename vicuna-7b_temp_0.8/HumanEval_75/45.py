
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a = int(a)
    if a < 0:
        return False
    elif a == 0:
        return True
    elif a == 1:
        return False
    else:
        prime_1 = is_prime(a-1)
        prime_2 = is_prime(a-2)
        prime_3 = is_prime(a-3)
        if prime_1 == True and prime_2 == True and prime_3 == True:
            return True
        else:
            return False
