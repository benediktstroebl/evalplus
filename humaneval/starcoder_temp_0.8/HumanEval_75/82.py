
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a == 0:
        return False
    elif a == 1:
        return False
    else:
        for i in range(2, 100):
            if a % i == 0:
                for j in range(2, 100):
                    if a % j == 0:
                        for k in range(2, 100):
                            if a % k == 0:
                                return False
