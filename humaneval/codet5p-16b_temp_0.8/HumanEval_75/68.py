
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    a_div = 2
    b_div = 3
    c_div = 5
    while True:
        if a % a_div == 0:
            if b % b_div == 0:
                if c % c_div == 0:
                    return True
        a_div += 1
        b_div += 1
        c_div += 1
        if a_div > c_div:
            return False

