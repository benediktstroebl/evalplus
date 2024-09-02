

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
    i = 1
    j = 2
    k = 3
    while i < n:
        while not is_prime(k):
            k += 1
            i += 1
        i += 1
        j += 1
        k += j
    return k

