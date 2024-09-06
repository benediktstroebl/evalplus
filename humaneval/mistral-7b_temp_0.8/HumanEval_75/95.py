
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a == 2 or a == 3 or a == 5:
        return True
    else:
        for num in range(2, a):
            if a % num == 0:
                if is_prime(num) and is_prime(a // num):
                    return True
        return False

