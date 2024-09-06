
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 30 or a > 99:
        return False
    else:
        prime_numbers = [2, 3, 5]
        for prime in prime_numbers:
            if a % prime == 0:
                a = a / prime
        if a != 1:
            return False
        return True
