

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
    fib_num = 1
    fib_prev = 1
    while fib_num < n:
        fib_next = fib_prev + fib_num
        fib_num = fib_prev
        fib_prev = fib_next
        if fib_next % 2 == 0:
            fib_next = fib_next + 1
        if fib_next % 3 == 0:
            fib_next = fib_next + 1
        if fib_next % 5 == 0:
            fib_next = fib_next + 1
        if fib_next % 7 == 0:
            fib_next = fib_next + 1
        if fib_next % 11 == 0:
            fib_next = fib_next + 1
        if fib_next % 13 == 0:
            fib_next = fib_next + 1
        if fib_next % 17 == 0:
            fib_next = fib_next + 1
        if fib_next % 19 == 0:
            fib_next = fib_next
