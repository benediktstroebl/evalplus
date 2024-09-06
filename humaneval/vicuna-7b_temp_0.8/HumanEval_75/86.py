
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 100:
        for p1 in range(2, int(a ** 0.5) + 1):
            for p2 in range(p1, int(a ** 0.5) + 1):
                if a % p1 == 0 and a % p2 == 0:
                    return False
            if a % p1 == 0:
                return False
        return True
    else:
        return False
