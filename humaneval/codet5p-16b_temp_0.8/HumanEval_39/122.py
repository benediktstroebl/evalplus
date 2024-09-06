

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

    fib_n = 1
    fib_prev = 1
    fib_next = 0

    for i in range(3, n + 1):
        fib_next = fib_prev + fib_n
        fib_n = fib_prev
        fib_prev = fib_next

    return fib_next
