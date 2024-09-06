
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    for i in range(3, a, 2):
        if is_prime(i):
            for j in range(3, a, 2):
                if is_prime(j) and i * j == a:
                    return True
    return False
