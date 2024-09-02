
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    x = True
    n = 2
    while n*n <= a:
        if a % n == 0:
            x = False
            break
        n += 1
    return x

