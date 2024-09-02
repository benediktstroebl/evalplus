
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(a):
        if a < 2:
            return False
        for i in range(2, a//2):
            if a % i == 0:
                return False
        return True
    for x in range(1, int(a**0.5)+1):
        if is_prime(x) and is_prime(a/x):
            return True
    return False
