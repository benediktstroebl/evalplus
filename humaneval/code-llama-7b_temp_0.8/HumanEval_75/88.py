
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = [2, 3, 5, 7]
    for i in primes:
        if i == 2:
            if a % 2 == 0:
                a /= 2
                continue
            else:
                return False
        elif i == 3:
            if a % 3 == 0:
                a /= 3
                continue
            else:
                return False
        elif i == 5:
            if a % 5 == 0:
                a /= 5
                continue
            else:
                return False
        elif i == 7:
            if a % 7 == 0:
                a /= 7
                continue
            else:
                return False
    return True
