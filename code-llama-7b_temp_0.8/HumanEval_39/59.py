

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
    if n < 1:
        return 2
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        # print('call prime_fib({})'.format(n - 2))
        a = prime_fib(n - 2)
        # print('call prime_fib({})'.format(n - 1))
        b = prime_fib(n - 1)
        while (not is_prime(a + b)) or (not is_prime(b)):
            a = b
            b = a + b
        return b

