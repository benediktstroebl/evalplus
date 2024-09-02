

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
    if n < 1:
        return None

    def is_prime(x: int) -> bool:
        if x < 2:
            return False

        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False

        return True

    if is_prime(1):
        return 2

    if is_prime(2):
        return 3

    F0 = 1
    F1 = 2
    F2 = 3
    n = 2
    is_prime(F2)

    while n < n:
        if is_prime(F2):
            return F2

        F0, F1, F2 = F1, F2, F1 + F2
        n += 1

