from itertools import count
primes = [2, 3]
def is_prime(n):
    """
    Determines whether n is prime
    """
    if n < 4:
        return n > 1
    for i in primes:
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime
    """
    if n <= 0:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev, curr = 2, 3
    num = next((i for i in count(prev, curr) if is_prime(i)), None)
    return num