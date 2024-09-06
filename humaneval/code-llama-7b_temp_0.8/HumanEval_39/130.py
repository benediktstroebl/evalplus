

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
    k = 0
    s = 0
    fib = []
    while s < n:
        fib.append(fibonacci(k))
        s += fib[-1]
        k += 1
    while not is_prime(fib[k - 1]):
        k -= 1
    return fib[k - 1]

