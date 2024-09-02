

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
    fib_1 = 1
    fib_2 = 2
    fib_n = fib_1 + fib_2
    is_prime = True
    while fib_n < n:
        if is_prime and fib_n % 2 == 0:
            is_prime = False
        else:
            fib_n = fib_1 + fib_2
            fib_1 = fib_2
            fib_2 = fib_n
    return fib_n

