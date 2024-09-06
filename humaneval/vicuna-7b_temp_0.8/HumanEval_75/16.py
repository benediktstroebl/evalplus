
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Check for prime factors less than a
    if a % 2 == 0:
        return False
    if a % 3 == 0:
        return False
    # Check for factors
    for i in range(5, int(a ** 0.5) + 1, 6):
        for j in range(i + 1, int(a ** 0.5) + 1, 6):
            if a % (i * j) == 0:
                return False
    return True
