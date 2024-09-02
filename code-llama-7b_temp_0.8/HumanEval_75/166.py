
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a == 0 or a == 1:
        return False

    def is_prime(x):
        if x == 0 or x == 1:
            return False
        elif x == 2:
            return True
        else:
            for i in range(2, int(x**0.5)+1):
                if x%i == 0:
                    return False
            return True

    if is_prime(a) == True:
        return False

    if a%2 == 0:
        a = a/2

    if is_prime(a) == True:
        return False

    if a%3 == 0:
        a = a/3

    if is_prime(a) == True:
        return False

    if a%5 == 0:
        a = a/5

    if is_prime(a) == True:
        return False

    return True
