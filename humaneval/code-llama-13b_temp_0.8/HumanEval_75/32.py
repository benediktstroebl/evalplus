
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for n1 in range(1, a):
        if a % n1 == 0:
            for n2 in range(1, n1):
                if n1 % n2 == 0:
                    for n3 in range(1, n2):
                        if n2 % n3 == 0:
                            if n3 == n1:
                                return True
                            else:
                                break
    return False
