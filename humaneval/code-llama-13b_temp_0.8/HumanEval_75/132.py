
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    # your code here
    x = 2
    if a < 3:
        return False
    while a > 1:
        if a % x == 0:
            a /= x
            x = 2
        else:
            x += 1
        if x > 100:
            return False
    return True
