

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
    # 1 <= n <= 10^5
    if n <= 2:
        return n

    if n % 2 == 0:
        return 3

    elif n == 3:
        return 5

    else:
        p1 = prime_fib(n // 2)
        p2 = prime_fib(n // 2 + 1)
        for i in range(3, n + 1):
            if p1 * p2 > i:
                return i
        return 2  # No prime found
