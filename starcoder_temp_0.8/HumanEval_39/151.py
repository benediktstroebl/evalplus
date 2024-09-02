

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

    def is_prime(n: int) -> bool:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def fib(n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return a

    f = 0
    for i in range(n):
        if is_prime(fib(f)):
            f += 1
    return fib(f-1)
