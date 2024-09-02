

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    # check if n is prime
    if n < 2:
        raise ValueError("n must be greater than 1")
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    # check the rest of the conditions
    # if n % 5 == 0, n is divisible by 5, so it's not a prime
    if n % 5 == 0:
        return 5
    # check the rest of the conditions
    # if n % 7 == 0, n is divisible by 7, so it's not a prime
    if n % 7 == 0:
        return 7
    # check the rest of the conditions
    # if n % 11 == 0, n is divisible by 11, so it's not a prime
    if n % 11 == 0:
        return 11
    # check the rest of the conditions
    # if n % 13 == 0, n is divisible by 13, so it's not a prime
    if n % 13 == 0:
        return 13
    # check the rest of the conditions
    # if n % 14 == 0, n is divisible by 14, so it's not a prime
    if n % 14 == 0:
        return 14
    # check the rest of the conditions
    # if n % 16 == 0, n is divisible by 16, so it's not a prime
    if n % 16 == 0:
        return 16
    # check the rest of the conditions
    # if n % 19 == 0, n is divisible by 19, so it's not a prime
    if n % 19 == 0:
        return 19
    # check the rest of the conditions
    # if n % 20 == 0, n is divisible by 20, so it's not a prime
    if n % 20 == 0:
        return 20
    # check the rest of the conditions
    
