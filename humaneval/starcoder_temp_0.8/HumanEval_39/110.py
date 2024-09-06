

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

    for i in range(n + 1):
        prime = True
        fib = fibonacci(i)
        for j in range(2, fib):
            if fib % j == 0:
                prime = False
                break
        if prime:
            return fib
