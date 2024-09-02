
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def _is_multiply_prime(a, b):
        if a <= 100:
            for p in range(b, 101, 2):
                if a % p == 0:
                    return False
            return True

    return _is_multiply_prime(a, a)
