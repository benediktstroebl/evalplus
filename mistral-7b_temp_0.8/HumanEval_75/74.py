
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Base cases
    if a == 1: return False
    if a == 2 or a == 3 or a == 5: return True

    # Recursion case
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            if is_multiply_prime(i) and is_multiply_prime(a // i):
                return True
            else:
                return False
    return False
