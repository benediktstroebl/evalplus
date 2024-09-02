
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    # check if a is prime
    if a < 2:
        return False
    elif a == 2:
        return True
    else:
        for i in range(3, int(a**0.5) + 1, 2):
            for j in range(2, int(a**0.5) + 1, 2):
                if (a - i - j) % i == 0 or (a - i - j) % j == 0:
                    return False
        return True
