

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
    if n <= 2:
        return 2
    elif n == 3:
        return 3
    else:
        if fib(n-1) % 2 == 0:
            return 0
        elif fib(n-1) % 2 == 1:
            return 2
        elif fib(n-2) % 2 == 0:
            return fib(n-2) + fib(n-3)
        elif fib(n-2) % 2 == 1:
            return fib(n-2) + 2
        else:
            for i in range(n):
                if fib(i) % 2 == 0:
                    return 0
                elif fib(i) % 2 == 1:
                    return fib(i) + 2
            return 2
