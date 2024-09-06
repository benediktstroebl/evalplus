
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(x):
        if x < 2:
            return False
        for y in range(2, x):
            if x % y == 0:
                return False
        return True

    def is_multiple_of(y, x):
        if y == 0:
            return True
        if y == 1:
            return False
        for z in range(y, x):
            if x % z == 0:
                return True
        return False

    def is_multiply_prime(a):
        if a < 3:
            return True
        if a % 2 == 0:
            return False
        for b in range(3, int(a ** 0.5) + 1, 2):
            if is_prime(b) and is_multiple_of(a, b):
                return False
        return True

    return is_multiply_prime(a)