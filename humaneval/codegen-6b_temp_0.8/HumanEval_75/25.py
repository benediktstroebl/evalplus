
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for i in range(3, 100):
        if a % i == 0:
            for j in range(3, i):
                if i % j != 0:
                    mult = i * j
                    if mult < 100:
                        if mult % 3 != 0:
                            return False
            return True
        else:
            return False
