

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
    if n < 2 or n > 100:
        return 0
    if n % 2 != 0:
        return 0
    if n not in [2, 3]:
        for i in range(4, int(n ** 0.5) + 1, 2):
            if (n - i) % i != 0:
                return 0
        return int(n ** 0.5) + 1
    elif n in [5, 89]:
        for i in range(4, int(n ** 0.5) + 1, 2):
            if (n - i) % 2 == 0:
                for j in range(i, int(n ** 0.5) + 1, 2):
                    if (n - i - j) % i == 0:
                        return 0
        return int(n ** 0.5) + 1
    else:
        return 0
