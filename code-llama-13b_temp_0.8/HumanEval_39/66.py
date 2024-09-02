

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
    if n == 1:
        return 2

    fibs = [2]
    prime_fibs = []
    while len(prime_fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
        if is_prime(fibs[-1]):
            prime_fibs.append(fibs[-1])

    return prime_fibs[n-1]

