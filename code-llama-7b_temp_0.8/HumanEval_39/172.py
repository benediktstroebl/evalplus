

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
    if n == 1:
        return 2
    elif n == 2:
        return 3

    def is_prime(n: int) -> bool:
        if n == 2:
            return True
        elif n < 2 or n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def fib(n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 1
        return fib(n - 1) + fib(n - 2)

    def check_is_prime(n: int, x: int, y: int):
        if is_prime(x + y):
            return x + y
        return check_is_prime(n, y, x + y)

    return check_is_prime(n, fib(1), fib(2))

