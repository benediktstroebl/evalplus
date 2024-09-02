
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # Try to find factors of a
    n = a
    for i in range(1, 100):
        for j in range(i + 1, 100):
            if (n % (i * j)) == 0:
                return False
        if (n % i) == 0:
            return False
    return True
