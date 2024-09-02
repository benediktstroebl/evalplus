
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    n = int(a)
    p1 = 2
    p2 = 3
    p3 = 5
    for i in range(n-1):
        for j in range(i+1, n):
            if (n % j == 0):
                return False
        p2 = 2
        p3 = 3
    return True