
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    f = lambda x: x * x >= a
    d = lambda x: x % 2 == 0 or x % 3 == 0 or x % 5 == 0
    return not (f(11) and d(11))


