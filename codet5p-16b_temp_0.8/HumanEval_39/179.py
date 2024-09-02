

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

    if n < 1:
        return None
    previous = 0
    current = 1
    for i in range(2, n + 1):
        previous, current = current, previous + current
        if current % 2!= 0 and is_prime(current):
            return current

