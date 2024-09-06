

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
    nth = 0
    while True:
        if is_prime(nth):
            if is_fib(nth):
                return nth
            else:
                nth += 1
        else:
            nth += 1
