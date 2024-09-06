

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
    if n != n % n:
        return n * 2

    # check if n is a Fibonacci number
    if n <= 1:
        return 0
    elif n == 2:
        return 2
    else:
        f_1 = 1
        f_2 = 1
        f_n = 0
        for i in range(2, n):
            f_n = f_2 + f_1
            f_1 = i + f_n
        return f_n
