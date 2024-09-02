
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    i = 3
    is_prime = False
    while i * i < a:
        if a % i == 0:
            is_prime = False
            return is_prime
            break
        i += 2
        is_prime = True
    return is_prime
