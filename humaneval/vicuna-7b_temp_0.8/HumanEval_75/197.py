
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a_prime = 2
    while a_prime * a_prime <= a:
        a_prime = a_prime + 6

    if a % 2 == 0:
        return False

    for i in range(3, int(a**0.5) + 1, 2):
        if a % i == 0:
            return False

    return True
