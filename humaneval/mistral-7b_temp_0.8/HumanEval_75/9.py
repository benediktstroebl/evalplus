
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    x = 2
    is_prime = True
    count = 0
    if (a % 2 == 0):
        return False
    while (x * x <= a):
        if (a % x == 0):
            count += 1
            while (a % x == 0):
                a /= x
                count -= 1
        x += 1
    if (count != 3):
        is_prime = False
    return is_prime

