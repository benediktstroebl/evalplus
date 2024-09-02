
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # your code here
    num_primes = 0
    factor = 2
    # a = 30
    # 2 is a prime number, so it can be a factor,
    # so we will have to check only up to a/2
    while a > 1:
        while a % factor == 0:
            num_primes += 1
            a /= factor
        factor += 1
    return num_primes == 3

