
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for i in range(1, a//3):
        if a % i == 0:
            if i == 2 or i == 3 or i == 5:
                continue
            else:
                return False
    return True

