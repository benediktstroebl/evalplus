

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
        return 2
    elif n < 4:
        return 1
    elif n == 4:
        return 3
    elif n == 5:
        return 5
    elif n % 2 == 0:
        return 3
    elif n % 3 == 0:
        return 5
    else:
        for i in range(4, int(n ** 0.5) + 1, 2):
            for j in range(i + 1, int(n ** 0.5) + 1, 2):
                if (i ** 2 + j ** 2) % n == 0:
                    return 0
        return 1

