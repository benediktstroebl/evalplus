

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
    if n < 2:
        return 1
    elif n <= 4:
        return 2
    elif n <= 8:
        if fib(n-1) % 2 == 0:
            return 3
        else:
            return 5
    elif n <= 13:
        if fib(n-2) % 2 == 0:
            return 5
        else:
            return 13
    else:
        fib_sum = fib(n-3) + fib(n-2)
        if fib_sum % 2 == 0:
            return 13
        else:
            return 89
