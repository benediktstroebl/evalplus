
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    is_prime = 0
    for num in range(2, 100):
        if a % num == 0:
            is_prime += 1
            if is_prime > 2:
                return False
    if is_prime == 2:
        return True
