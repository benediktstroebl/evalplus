
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a <= 0:
        return False
    if a == 1:
        return False
    sq = int(a**0.5) + 1
    primes = [x for x in range(2, sq) if a % x == 0]
    if len(primes) >= 3:
        return True
    return False
    
