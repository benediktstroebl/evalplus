

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

    counter = 1
    fib = 1
    while True:
        if is_prime(fib) and is_prime(fib+1):
            counter += 1
            if counter == n:
                return fib
        fib += 1
