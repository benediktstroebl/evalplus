
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # TODO: Write code here
    i = 2
    while i < a:
        if is_prime(a) and a / i == 1:
            return True
        i += 1
    return False
