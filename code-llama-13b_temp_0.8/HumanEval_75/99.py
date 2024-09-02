
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
    
    for n in range(2, a+1):
        if a % n == 0:
            counter = 0
            while a % n == 0:
                counter += 1
                a /= n
            if counter > 1 and n != 1:
                return False
    return True
