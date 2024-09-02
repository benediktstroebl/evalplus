

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

    prime_fib_cache = []

    nth_fib = fibonacci_seq(n)

    while is_prime(nth_fib) == False:
        prime_fib_cache.append(nth_fib)
        nth_fib = fibonacci_seq(n)

    prime_fib_cache.append(nth_fib)
    return prime_fib_cache

