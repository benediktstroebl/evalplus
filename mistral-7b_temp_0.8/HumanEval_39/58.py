

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
    fibs = []
    fib = 1
    fib_prev = 0
    while True:
        fib_next = fib + fib_prev
        fibs.append(fib)
        if fib_next > n:
            if fib % n == 0:
                return fib
            elif fib_prev % n == 0:
                return fib_prev
            else:
                return None
        fib_prev, fib = fib, fib_next

