

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    "*** YOUR CODE HERE ***"
    def is_prime(n):
        if n <= 3:
            return n == 2 or n == 3
        elif n % 2 == 0:
            return False
        elif n % 3 == 0:
            return False
        i = 5
        while i*i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    i = n-1
    while i+1 > 1:
        if n % i == 0 and is_prime(i):
            return i
        i -= 1
