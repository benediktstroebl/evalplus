

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
    if n <= 1:
        return 2
    else:
        f1 = fib(n-1)
        f2 = fib(n-2)
        if (f1 % 2) == 0:
            return f1
        else:
            if (f2 % 2) == 0:
                return f2
            else:
                for i in range(3, int(n**0.5) + 1, 2):
                    if f1 % i == 0:
                        return f1
                    if f2 % i == 0:
                        return f2
                    else:
                        return i
