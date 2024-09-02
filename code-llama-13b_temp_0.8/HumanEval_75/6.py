
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        i = 2
        while i < a:
            if (a % i == 0):
                j = 2
                while (j < i):
                    if (i % j == 0):
                        break
                    j += 1
                if (j > i):
                    return False
            i += 1
        return True
    else:
        return False
        
