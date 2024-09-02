
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(n, a, b):
        if n <= 1:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 3):
            if n % i == 0:
                return False
        return True
    
    def is_multiply_prime(n, a, b):
        c = a * b
        for i in range(2, int(c**0.5) + 1, 2):
            if is_prime(c, i, a*b) or is_prime(c, i, b):
                return False
        return True
    
    return is_multiply_prime(a, 3, 5)
