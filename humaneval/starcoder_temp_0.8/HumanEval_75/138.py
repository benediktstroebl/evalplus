
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for n in range(2, 100):
        if n > 1:
            for x in range(2, n):
                if n % x == 0:
                    break
            else:
                if a % n == 0 and a!= n:
                    return True
    return False
