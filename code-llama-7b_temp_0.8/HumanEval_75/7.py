
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    def is_prime(a):
        if a < 2:
            return False
        if a < 4:
            return True

        for i in range(2, int(a**0.5)+1):
            if a % i == 0:
                return False
        return True

    if a < 30:
        return False
    for i in range(2, 10):
        if is_prime(a//i):
            if is_prime((a//i)//i):
                if is_prime((a//i)//i//i):
                    return True
    return False
