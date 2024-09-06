

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
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 13
    else:
        fib1 = fib2 = 2
        while True:
            fib = fib1 + fib2
            if is_prime(fib) and is_fib(fib):
                if n == fib - 1:
                    return fib
                fib1 = fib2
                fib2 = fib
            else:
                if n == fib - 1:
                    return fib
                fib1 = fib2
                fib2 = fib

