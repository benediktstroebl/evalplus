
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    a_count = 0
    i = 2
    while i < a:
        if a % i == 0:
            a_count += 1
            if a_count == 3:
                return True
        i += 1
    return False
