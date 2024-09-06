
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    is_prime = False
    i = 2
    while i ** 2 <= a:
        if a % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
        i += 1
    if is_prime:
        i -= 1
        if a % i == 0:
            is_prime = False
    return is_prime


