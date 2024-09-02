

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
    if n < 2:
        return 1
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n % 2 == 0:
        return 1
    else:
        for i in range(1, int(n ** 0.5) + 1):
            for j in range(2, int(n ** 0.5) + 1):
                if (j ** 2 - j - i) % n == 0:
                    return None
        return n