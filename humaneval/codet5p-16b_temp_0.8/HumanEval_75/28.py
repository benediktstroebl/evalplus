
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    primes = [2,3,5,7,11]
    for i in range(0, len(primes)):
        for j in range(0, len(primes)):
            if (primes[i] * primes[j] == a):
                return True
    return False

