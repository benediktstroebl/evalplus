
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    factors = []
    for i in range(1, int(a**0.5) + 1):
        for j in range(i, a):
            if a % j == 0:
                break
        else:
            factors.append(i)
    
    for i in factors:
        if not is_prime(i):
            return False
    return True
