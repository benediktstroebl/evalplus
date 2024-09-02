
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # check divisibility by 2
    if a % 2 == 0:
        return False
    # check divisibility by 3
    if a % 3 == 0:
        return False
    # check divisibility by 5
    if a % 5 == 0:
        return False
    # check divisibility by 7
    if a % 7 == 0:
        return False
    # check divisibility by 11
    if a % 11 == 0:
        return False
    
    # if we reach this point, the number is not divisible by any of the given numbers, so it is prime
    return True

print(is_multiply_prime(30)) # True