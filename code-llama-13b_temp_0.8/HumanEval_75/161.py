
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for a in range(1, 100):
        is_multiply_prime = False
        for b in range(1, 100):
            for c in range(1, 100):
                if a == (b * c):
                    is_multiply_prime = True
                    return is_multiply_prime
                else:
                    pass
    return False
