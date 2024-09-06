
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100:
        is_prime = True
        for number in range(2, a):
            if a % number == 0:
                is_prime = False
                break
        if is_prime:
            return True
    return False
