
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    p = 2
    q = 3
    for i in range(a-1, max(p-1, 0), -1):
        if (a % i) == 0:
            return False
    if a % p == 0:
        return False
    p = 5
    q = 2
    for i in range(a-1, max(q-1, 0), -1):
        if (a % i) == 0:
            return False
    if a % q == 0:
        return False
    return True
