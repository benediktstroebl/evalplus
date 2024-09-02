
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    """ your code here """
    """
    prime_list = []
    if a<10:
        if a == 3 or a == 5 or a == 7:
            return True
    elif a<100:
        if a % 2 == 0:
            return False
        for i in range(3, 10):
            if a % i == 0:
                return False
        return True
    else:
        return False
    """
    from math import sqrt
    if a<10:
        if a == 3 or a == 5 or a == 7:
            return True
    elif a<100:
        if a % 2 == 0:
            return False
        root = int(sqrt(a))
        for i in range(3,root+1):
            if a % i == 0:
                return False
        return True
    else:
        return False







