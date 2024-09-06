
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # FIRST_PRIME = 2
    # SECOND_PRIME = 3
    # THIRD_PRIME = 5
    FIRST_PRIME = 3
    SECOND_PRIME = 5
    THIRD_PRIME = 7

    multiplier = FIRST_PRIME

    while multiplier < a:
        multiplier = multiplier * SECOND_PRIME
        if multiplier == a:
            return True
        elif multiplier > a:
            return False

    return False
