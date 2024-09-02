
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    n = int(a)
    if n < 1:
        return False
    for i in range(2, n + 1):
        for j in range(i, n + 1):
            p = prime(j)
            for k in range(i, p + 1):
                q = prime(k)
                if (a % (p * q)) == 0:
                    return False
    return True