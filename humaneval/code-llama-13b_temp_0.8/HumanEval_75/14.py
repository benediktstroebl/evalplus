
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for i in range(2,11):
        if (a % i == 0):
            c = a / i
            for j in range(2,11):
                if (c % j == 0):
                    b = c / j
                    for k in range(2,11):
                        if (b % k == 0):
                            d = b / k
                            if (d % k == 0):
                                return True
    return False
