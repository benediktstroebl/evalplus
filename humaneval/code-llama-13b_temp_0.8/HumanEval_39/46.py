

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
    f0 = 0
    f1 = 1
    i = 0
    while True:
        i += 1
        f0, f1 = f1, f0 + f1
        if is_prime(f1) == True:
            i += 1
            if i == n:
                return f1

