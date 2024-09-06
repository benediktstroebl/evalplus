

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

    p, f = 2, 1
    while p <= n:
        f = (p * f) + (p - f)
        p += 1
        if f > n:
            break
        if f > 1:
            for i in range(2, int(f ** 0.5) + 1):
                if f % i == 0:
                    break
            else:
                return f
    return None

