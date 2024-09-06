
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a_str = str(a)
    l = len(a_str)
    i = 0
    while i < l:
        if a_str[i] != "0":
            if is_prime(int(a_str[i])) == True:
                if l > 1:
                    if a_str[i+1] != "0":
                        if is_prime(int(a_str[i+1])) == True:
                            if l > 2:
                                if a_str[i+2] != "0":
                                    if is_prime(int(a_str[i+2])) == True:
                                        return True
    return False
