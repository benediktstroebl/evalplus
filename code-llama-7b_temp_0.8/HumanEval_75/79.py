
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    num = 1
    i = 2
    while i <= a:
        if (a % i == 0):
            num += 1
            j = i + 1
            while j <= a:
                if (a % j == 0):
                    num += 1
                    k = j + 1
                    while k <= a:
                        if (a % k == 0):
                            num += 1
                            if num == 4:
                                return True
                            else:
                                k += 1
                        else:
                            k += 1
                else:
                    j += 1
        else:
            i += 1
    return False
