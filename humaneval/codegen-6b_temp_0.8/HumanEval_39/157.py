

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
    if n < 0:
        raise ValueError("negative number passed to prime_fib")

    # the fibonacci number generator
    fib_nums = lambda n: (fib_nums(n - 1) + fib_nums(n - 2)) % 10

    # the prime sieve
    primes = [False, False] + [True] * ((n - 1) // 2)

    fib_num = 0
    while primes[fib_num]:
        fib_num = fib_nums(fib_num)
    return fib_num

