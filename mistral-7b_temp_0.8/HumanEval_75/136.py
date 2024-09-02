
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    is_divisble_by_3 = False
    is_divisble_by_5 = False
    # check divisibility
    for i in range(1, 3):
        if a % i == 0:
            is_divisble_by_3 = True
    for i in range(1, 5):
        if a % i == 0:
            is_divisble_by_5 = True
    if is_divisble_by_3 and is_divisble_by_5:
        return True
    else:
        return False
