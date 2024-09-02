
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    count = 0
    if is_prime(a):
        if is_prime(a/2):
            if is_prime(a/3):
                count += 1
        if is_prime(a/3):
            count += 1
    if count == 2:
        return True
    else:
        return False
