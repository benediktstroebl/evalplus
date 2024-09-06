
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # check if a is prime
    if a % 2 != 0:
        return False
    if a % 3 == 0:
        return False
    # check if a is divisible by 5
    if a % 5 == 0:
        return False
    # check if a is divisible by 7
    if a % 7 == 0:
        return False
    # check if a is divisible by 11
    if a % 11 == 0:
        return False

    # if all the above conditions are not met, then the number is prime
    return True

