

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
        return n
    if n % 2 == 0:
        return 0
    elif n > 1:
        x, y = 1, 1
        while x < n:
            if x % 2 == 0:
                x *= 2
                x *= 2
                continue
            if y % 2 == 0:
                y *= 2
                y *= 2
                continue
            x = x + y
            y = x + y
        if (x ** 2 - y ** 2) % n == 0:
            return 0
        if not is_prime(x):
            return 0
        return x
