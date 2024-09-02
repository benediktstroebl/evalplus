

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
    if n == 1 or n == 2:
        return n
    elif n <= 0:
        raise ValueError('n must be a positive integer')
    elif n >= 3:
        pass
    else:
        return -1
    i = 0
    x, y = 1, 1
    while 1:
        if y % 2 == 0:
            y += 1
        else:
            break
        if is_prime(y):
            return y
