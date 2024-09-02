
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a > 100:
        return False
    factors = []
    for i in range(1, a):
        if a % i == 0:
            factors.append(i)
    if len(factors) != 3:
        return False
    for i in factors:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if not is_prime:
            return False
    return True
