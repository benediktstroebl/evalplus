

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

    count = 2
    n1, n2 = 1, 1
    while count < n:
        n1, n2 = n2, n1 + n2
        if not is_prime(n2):
            n2 = n2 - 1
        count += 1
    return n2

