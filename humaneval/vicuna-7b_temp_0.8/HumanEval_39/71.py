

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
    elif n < 15:
        fib = fibonacci(n)
        if fib % 2 == 0:
            return 1
        else:
            return fib
    elif n < 40:
        fib = fibonacci(n)
        if fib % 2 == 0:
            return 1
        else:
            for i in range(2, n):
                if fib % i == 0:
                    return 1
            return fib
    elif n < 100:
        fib = fibonacci(n)
        if fib % 2 == 0:
            return 1
        else:
            for i in range(2, n):
                if fib % i == 0:
                    return 1
            for j in range(3, n, 2):
                if fib % j == 0:
                    return 1
            return fib
    elif n < 500:
        fib = fibonacci(n)
        if fib % 2 == 0:
            return 1
        else:
            for i in range(2, n):
                if fib % i == 0:
                    return 1
            for j in range(3, n, 2):
                if fib % j == 0:
                    return 1
            for k in range(5, n, 2):
                if fib % k == 0:
                    return 1
            return fib
    else:
        fib = fibonacci(n)
        if fib % 2 == 0:
            return 1
        else:
            for i in range(2, n):
                if fib % i == 0:
                    return 1
            for j in range(3, n, 2):
                if fib % j == 0:
                    return 1
            for k in range(5, n, 2):
                if fib % k == 0:
                    return 1
            for l in range(7, n, 2):
                if fib % l == 0:
                    return 1
            return fib
