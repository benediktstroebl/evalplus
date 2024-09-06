

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
    index = 1
    prev = 1
    cur = 2
    while index < n:
        prev, cur = cur, cur + prev
        if isprime(cur):
            index += 1
    return cur
