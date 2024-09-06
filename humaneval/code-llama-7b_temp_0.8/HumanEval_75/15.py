
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    # prime numbers to check
    primes = [2, 3, 5]

    # check that each prime number divide a
    for prime in primes:
        if a % prime != 0:
            return False

    # divide a by the prime numbers
    while a > 1:
        for prime in primes:
            if a % prime == 0:
                a = a / prime

    # check that a is 1
    if a == 1:
        return True

    return False

