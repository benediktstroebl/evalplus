
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for x in range(a-1):
        for y in range(x+1, a+1):
            for z in range(y+1, a+1):
                if x**2 + y**2 == z**2:
                    return False
    return True
