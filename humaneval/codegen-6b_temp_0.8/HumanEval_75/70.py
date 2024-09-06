
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    prime = 2
    while prime < a:
        if a % prime == 0:
            if is_prime(a / prime):
                return True
        prime += 1
    return False
