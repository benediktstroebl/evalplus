

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    def factorial(n):
        if n <= 1:
            return 1
        else:
            return n * factorial(n - 1)
    def prime(n):
        if n % 2 == 0 or n % 3 == 0:
            return False
        else:
            i = 5
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 2
            return True
    a = 2
    b = n - 1
    while a < b:
        if n % a == 0:
            b = n // a
            if prime(b):
                return b
        a += 1
    return a
