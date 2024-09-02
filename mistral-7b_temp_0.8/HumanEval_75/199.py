
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    def is_prime(x):
        if x % 2 == 0: return False
        for i in range(3, x // 2, 2):
            if x % i == 0:
                return False
        return True

    return all(is_prime(x) for x in range(3, a // 2, 2))

