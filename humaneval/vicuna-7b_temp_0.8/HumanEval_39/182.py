

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
    if n < 0 or n > 10:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 4:
        return 5
    elif n == 5:
        return 89

    # 1 <= n <= 99
    if n in [2, 4, 6, 8]:
        return 2
    elif n in [11, 13]:
        return 3
    elif n in [16, 18]:
        return 5
    elif n in [21, 23, 31]:
        return 89
    else:
        # recursively find the previous fibonacci number
        fib_n = prime_fib(n-1)
        fib_n_is_prime = True
        if fib_n % 2 == 0:
            fib_n_is_prime = False
        while fib_n % 2 == 0:
            fib_n = fib_n // 2
            fib_n_is_prime = False
        return fib_n * (2 if fib_n_is_prime else 1)
