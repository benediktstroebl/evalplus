def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 100 and a > 1:
        # checking for factors
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                return False
        
        # edge case for factors
        if a == 3:
            return True
        
        for i in range(2, int(a**0.5) + 1):
            if a % i == 0:
                return False
        
        if a != 3:
            return True
    return False