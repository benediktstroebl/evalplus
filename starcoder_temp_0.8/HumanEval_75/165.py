
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for i in range(1, 100):
        if i % 3 == 0:
            for j in range(1, 100):
                if j % 5 == 0:
                    if i * j == a:
                        return True
    return False
