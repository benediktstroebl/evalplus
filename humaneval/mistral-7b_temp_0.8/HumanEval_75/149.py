
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for x in range(1, 100):
        for y in range(1, 100):
            for z in range(1, 100):
                if x * y * z == a:
                    if is_prime(x) and is_prime(y) and is_prime(z):
                        return True

    return False

