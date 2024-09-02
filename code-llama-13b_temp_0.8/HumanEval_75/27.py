
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a == 1 or a == 0:
        return False
    factors = []
    for i in range(2, a + 1):
        if a % i == 0:
            factors.append(i)
    for i in range(len(factors)):
        if factors[i] > 100:
            return False
        if factors[i] != 2 and factors[i] != 3 and factors[i] != 5 and is_prime(factors[i]) == False:
            return False
    return True
    
