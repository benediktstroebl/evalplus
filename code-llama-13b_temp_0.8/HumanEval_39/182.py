

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

    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        if num % 2 == 0:
            return num == 2
        return all(num % i for i in range(3, int(num ** 0.5 + 1), 2))

    phi = (1 + 5 ** 0.5) / 2
    m = n * phi
    a, b = 0, 1
    while b <= m:
        a, b = b, a + b

    return a - b if is_prime(a) else prime_fib(n - 1)

