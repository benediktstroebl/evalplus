
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    n = int(a)
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        for j in range(i + 1, n):
            if (n % i == 0 or n % j == 0):
                return False
        if (n % (i - 1) == 0 and n % (i + 1) == 0):
            return False
    return True
