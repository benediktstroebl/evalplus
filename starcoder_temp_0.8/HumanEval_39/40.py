

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
    if n in [1, 2]:
        return 2
    def is_prime(x: int) -> bool:
        return len([1 for i in range(2, x) if x % i == 0]) == 0

    i = 3
    while True:
        if is_prime(i):
            fib = fibonacci(i)
            if fib >= n:
                return fib
        i += 1
