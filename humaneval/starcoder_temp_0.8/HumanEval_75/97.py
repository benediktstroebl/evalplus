
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    
    if not (1 < a < 100):
        return False
    else:
        for i in range(2,a):
            if a%i == 0:
                if i == 2:
                    if a/2 in range(2,100):
                        continue
                    else:
                        return False
                elif i == 3:
                    if a/3 in range(2,100):
                        continue
                    else:
                        return False
                elif i == 5:
                    if a/5 in range(2,100):
                        continue
                    else:
                        return False
                else:
                    return False
    return True
