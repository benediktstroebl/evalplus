
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a == 1:
        return False
    n = a
    count = 0
    i = 2
    while n > 1:
        while n % i == 0:
            count += 1
            n /= i
        if count > 0:
            i += 1
        else:
            i += 1
    if count == 3:
        return True
    return False

