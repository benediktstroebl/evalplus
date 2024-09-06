
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    counter = 0
    for prime in primes:
        while a % prime == 0:
            counter += 1
            a /= prime
        if counter == 3:
            return True
    return False
