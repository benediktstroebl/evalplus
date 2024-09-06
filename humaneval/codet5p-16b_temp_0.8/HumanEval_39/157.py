

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

    fib_n_1 = 1
    fib_n_2 = 2
    i = 3
    while i <= n:
        fib_n_1, fib_n_2 = fib_n_2, fib_n_1 + fib_n_2
        i += 1
    is_prime = True
    fib_num = fib_n_2
    while is_prime and fib_num <= fib_n_2 + fib_n_1:
        is_prime = is_prime_number(fib_num)
        fib_num += fib_n_1
    return fib_num

