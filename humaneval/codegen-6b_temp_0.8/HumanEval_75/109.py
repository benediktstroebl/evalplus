
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, x + 1):
            if x % i == 0:
                return False
        return True
    for i in range(2, 100):
        if not is_prime(i) and not is_prime(i * 3) and not is_prime(i * 5):
            return False
    return True
