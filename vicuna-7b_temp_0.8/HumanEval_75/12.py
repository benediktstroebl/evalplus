
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # we will loop over a range of numbers from 2 to a
    # if we find 2 numbers that multiply to a and are both prime then we return True
    # else we return False
    for i in range(2, a):
        for j in range(i, a):
            if a % i == 0 or a % j == 0:
                return False
        if is_prime(a) and is_prime(i) and is_prime(j):
            return True
    return False