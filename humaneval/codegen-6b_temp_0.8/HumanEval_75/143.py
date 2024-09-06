
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = set(is_prime(a))
    if not primes:
        return False

    squared_primes = [i * i for i in primes]
    for i in squared_primes:
        if i > a:
            break
        s = set(is_prime(i))
        if not s:
            return False
    return True

