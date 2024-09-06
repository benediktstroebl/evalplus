
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if not a < 100:
        return "the number must be less than 100"
    # start of a function
    # 1- check that a is not a prime number
    if a < 3:
        return False

    # 2- check that a is not a multiple of 3 or 5
    if a % 3 == 0 or a % 5 == 0:
        return False

    # 3- check that a is a multiple of 3 and 5
    if a % 15 == 0:
        return False

    # 4- check that a is a multiple of 3 or 5
    for i in range(7, a):
        if a % i == 0:
            return False

    # 5- check that a is a multiple of 3 and 5
    if a % 3 == 0 and a % 5 == 0:
        return False

    return True
