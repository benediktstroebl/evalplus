

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
    # n is less than 1 (n = 0), raise exception
    if n < 1:
        raise ValueError('n must be positive')
    # if n is one, return the first prime, 2
    if n == 1:
        return 2
    # initialize variables
    a = 1
    b = 2
    c = a + b
    count = 1
    # while the Fibonacci number is less than n or not prime
    while count < n or is_prime(c) is False:
        a = b
        b = c
        c = a + b
        count += 1
    # return the Fibonacci number that is also prime
    return c

