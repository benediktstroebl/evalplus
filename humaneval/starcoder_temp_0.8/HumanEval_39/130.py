

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

    p_list = prime_list(n + 1)
    f_list = fib_list(n + 1)
    for i in range(n + 1):
        if f_list[i] > 10 ** 12:
            return p_list[i], f_list[i]
