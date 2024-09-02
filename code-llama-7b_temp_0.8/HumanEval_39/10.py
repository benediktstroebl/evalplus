

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
    fibs = [1, 1]
    for _ in range(n - 1):
        fibs.append(fibs[-1] + fibs[-2])

    is_prime = lambda x: all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
    while True:
        if is_prime(fibs[-1]):
            return fibs[-1]
        fibs.append(fibs[-1] + fibs[-2])
