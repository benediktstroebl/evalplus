

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
    # Only check even numbers, as all Fibonacci numbers are even
    if n % 2 == 0:
        return n
    else:
        fib = 0
        n //= 2
        while n > 1:
            fib += (n - 1) // 2
            n = n - 1
        for i in range(2, int(n ** 0.5) + 1, 2):
            if fib % i == 0:
                return None
        return fib
