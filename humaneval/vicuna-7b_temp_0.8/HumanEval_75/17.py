
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for x in range(2, int(a**0.5)+1):
        for y in range(x+1, a):
            z = a - y
            if (z % 2 == 0) or (z == a) or (a % 3 == 0):
                return False
    return True
