

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

    f_n = 0
    f_n_minus_one = 1
    f_n_minus_two = 1
    for i in range(n):
        f_n = f_n_minus_two + f_n_minus_one
        f_n_minus_two = f_n_minus_one
        f_n_minus_one = f_n
    while not is_prime(f_n):
        f_n = f_n + 1
    return f_n

