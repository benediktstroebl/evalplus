
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # is it greater than 1
    if a > 1:
        # is it a multiple of 3
        if a % 3 == 0:
            # is it a multiple of 5
            if a % 5 == 0:
                # is it a multiple of 7
                if a % 7 == 0:
                    return True
                # no multiple of 7
                return False
            # no multiple of 5
            return False
        # no multiple of 3
        return False
    # no greater than 1
    return False

