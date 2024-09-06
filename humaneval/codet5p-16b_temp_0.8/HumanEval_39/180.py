

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

    f_x, f_y = 0, 1
    while f_y < n:
        f_x, f_y = f_y, f_x + f_y
        if f_y > n:
            break
        if f_y > 1:
            for i in range(2, f_y):
                if f_y % i == 0:
                    break
            else:
                return f_y
    return 0

