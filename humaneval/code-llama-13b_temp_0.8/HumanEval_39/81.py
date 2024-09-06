

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
    memo = {1: 2, 2: 3, 3: 5}
    a, b = 2, 3

    while len(memo) < n:
        if is_prime(b) and is_fib(b):
            memo[len(memo) + 1] = b
        a, b = b, a + b

    return memo[n]

