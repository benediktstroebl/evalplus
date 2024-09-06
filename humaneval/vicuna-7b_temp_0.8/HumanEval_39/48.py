

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
    # skip first 2 numbers
    for i in range(2, n+1):
        # calculate fibonacci sequence
        fib = 0
        prev = 0
        for j in range(2, i+1):
            fib += prev
            prev = fib[1]
        # check primality
        if fib <= n**0.5:
            return 0
        if fib % 2 == 1:
            return 1
        if fib in (5, 8, 13, 21, 34, 55, 89):
            return fib
    return 0
