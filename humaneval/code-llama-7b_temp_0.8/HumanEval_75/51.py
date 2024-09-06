
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    import math
    primes = []
    if a <= 3:
        return False
    if a % 2 == 0 or a % 3 == 0:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            primes.append(i)
    if len(primes) >= 3 and len(set(primes)) == 3:
        return True
    return False

