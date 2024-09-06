

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
    k = 1
    n_fib = 2
    while k < n:
        n_fib += 1
        k += 1
        i = 2
        while i * i <= n_fib:
            if n_fib % i == 0:
                break
            i += 1
        else:
            k -= 1
    return n_fib

