

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

    fib = [1, 1]
    k = 0
    while k < n - 2:
        fib.append(fib[-2] + fib[-1])
        if is_prime(fib[-1]):
            k += 1
    return fib[-1]

