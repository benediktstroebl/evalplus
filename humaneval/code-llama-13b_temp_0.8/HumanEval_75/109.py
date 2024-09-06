
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    i = 2
    result = False
    while not result:
        if a % i == 0:
            s = i
            j = 2
            while j * j <= s and s != 1 and not result:
                if s % j == 0:
                    k = int(s/j)
                    if not is_prime(k):
                        result = False
                        break
                    elif k == 2 or k == 3 or k == 5:
                        result = True
                        break
                    else:
                        j += 1
                else:
                    j += 1
        else:
            i += 1
            
    return result
