
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    lst = [2, 3, 5]
    if (a < 100):
        for i in range(0, 3):
            if (a % lst[i]) == 0:
                a = a // lst[i]
            else:
                return False
        return True
    else:
        return False

