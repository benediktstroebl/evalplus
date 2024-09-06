
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """

    # use Sieve of Eratosthenes to check if the number is prime
    is_prime = [True for i in range(a)]
    for p in range(2, a):
        if (p % a) == 0:
            return False
        if (p > a // 2):
            sieve[a // 2] = True
            for i in range((a - 1) // 2), sieve[i] = True
    return True
