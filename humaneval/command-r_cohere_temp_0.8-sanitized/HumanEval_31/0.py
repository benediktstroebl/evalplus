def is_prime(n):
    """Returns true if n is a prime number, and false otherwise.
    Prime numbers are positive integers greater than 1 that have no positive divisors other than 1 and themselves.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True