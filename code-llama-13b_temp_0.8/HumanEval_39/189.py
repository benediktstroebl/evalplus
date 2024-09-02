

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
    # first number that is a Fibonacci number and it's also prime.
    # Fibonacci numbers
    fibo_prev: int = 1
    fibo: int = 1

    # iterates until the n-th prime Fibonacci number
    while n > 1:
        # swap fibo and fibo_prev
        fibo, fibo_prev = fibo + fibo_prev, fibo
        # Fibonacci number is prime if it doesn't have any even divisor
        if not (fibo % 2 == 0 or fibo % 5 == 0):
            n -= 1
    # returns the n-th prime Fibonacci number
    return fibo
