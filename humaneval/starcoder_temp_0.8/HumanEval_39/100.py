

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
    prev, curr = 1, 2
    for i in range(2, n + 1):
        prev, curr = curr, prev + curr
        while not is_prime(curr):
            curr = prev + curr
    return curr
