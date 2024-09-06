

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
    k = 2
    f_2 = 1
    f_1 = 2
    for i in range(3, n+1):
        f = f_1 + f_2
        f_2 = f_1
        f_1 = f
        while not is_prime(f):
            f = f_1 + f_2
            f_2 = f_1
            f_1 = f
        k += 1
    return f_1
