

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
    if n <= 0:
        raise ValueError("n must be >= 1.")
    elif n == 1:
        return 2
    prev, curr, i = 2, 3, 1
    while i < n:
        prev, curr = curr, prev + curr
        if is_prime(curr):
            i += 1
    return curr

