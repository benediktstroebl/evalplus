
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    if is_prime(3) and is_prime(5):
        if is_prime(a/3):
            return True
    else:
        return False
