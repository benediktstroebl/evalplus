

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

    if n == 2:
        return 3

    fib = [1, 2]
    i = 2
    while True:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
        if is_prime(fib[-1]):
            if i == n:
                return fib[-1]
            elif i > n:
                return fib[n - 1]

