
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 10:
        return True
    s = 1
    d = 1
    while d <= a:
        d = (d + a) % a
        s = s * s % a
    return s == 1
