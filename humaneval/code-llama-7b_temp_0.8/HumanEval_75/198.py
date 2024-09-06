
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # we know that a <= 99
    for num in range(2, 10):
        if num > a:
            return False
        # find if num is prime
        if is_prime(num):
            # check if a - num is also prime
            rest = a - num
            if is_prime(rest):
                # check if rest - num is also prime
                rest = rest - num
                if is_prime(rest):
                    return True
    return False
