
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a == 0:
        return False
    i = 2
    while i * i <= a:
        if a % i == 0:
            j = 2
            while j * j <= a // i:
                if a % j == 0 and j * j != a:
                    return False
                j += 1
            return True
        i += 1
    return False
