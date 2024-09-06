
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        return_value = False
        for i in range(2, 11):
            if (a % i == 0):
                rem = a % i
                for j in range(2, 11):
                    if (rem % j == 0):
                        rem = rem % j
                        for k in range(2, 11):
                            if (rem % k == 0):
                                rem = rem % k
                                if rem == 0:
                                    return_value = True
        return return_value
    else:
        return False
    
