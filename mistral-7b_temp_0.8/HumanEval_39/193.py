

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
    if n < 3:
        return n
    else:
        a = 1
        b = 1
        count = 1
        while True:
            if a % 2 == 0 and b % 2 == 0:
                count += 1
            if count > n - 3:
                return a
            else:
                a, b = b, a + b
        return None
