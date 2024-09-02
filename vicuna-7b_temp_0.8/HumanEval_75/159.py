
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    n = a
    while n >= 2:
        if n % 2 == 0:
            return False
        n = n - 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        j = 2
        while j < i:
            j = j + 6
        if n % (i * j) == 0:
            return False
        n = n - (i * j)
    return True
